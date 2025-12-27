var TimeLimitedCache = function() {
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
	const now = Date.now();
	const exists = this.cache.has(key) && now < this.cache.get(key).expiration;
	this.cache.set(key, {
		value: value,
		expiration: now + duration
	});
	return exists;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
	if (!this.cache.has(key)) {
		return -1;
	}
	const record = this.cache.get(key);
	if (Date.now() >= record.expiration) {
		this.cache.delete(key);
		return -1;
	}
	return record.value;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
	let count = 0;
	const now = Date.now();
	for (const [key, record] of this.cache.entries()) {
		if (now < record.expiration) {
			count++;
		} else {
			this.cache.delete(key);
		}
	}
	return count;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */