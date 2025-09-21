/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    /* Given a function fn and a time in milliseconds t, return a debounced version of that function. */
	/*
	For example, let's say t = 50ms, and the function was called at 30ms, 60ms, and 100ms.
	The first 2 function calls would be cancelled, and the 3rd function call would be executed at 150ms.
	If instead t = 35ms, The 1st call would be cancelled, the 2nd would be executed at 95ms, and the 3rd would be executed at 135ms.
	*/
    return function(...args) {
		if (this.timer) clearTimeout(this.timer);
		this.timer = setTimeout(() => {
			fn(...args);
		}, t);
    }
};
