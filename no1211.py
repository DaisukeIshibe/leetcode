import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
+--------------------------------+----------------------------------------------------+----------+--------+
| query_name                     | result                                             | position | rating |
| ------------------------------ | -------------------------------------------------- | -------- | ------ |
| pdxafib                        | jwqjgyrnhaptivvnqkj                                | 16       | 5      |
| mpzkxkzbompbpbavkb             | srlfyprermbgldweweulwdfmbddgarvtdm                 | 10       | 1      |
| udrcvuaxzjhbnvcyo              | hekmecxifwqthvcixhtnxnhjfzwuzbgirrljrdiz           | 14       | 3      |
| xdyoviczumlpchsnsbnwqmljgh     | kvrydrjdithfoytworvasqlyjulaolldallexqljk          | 3        | 4      |
| xdyoviczumlpchsnsbnwqmljgh     | qkebkugmaikexeuxnaruqrb                            | 19       | 2      |
| snhrdtzetlihfenkdjyatadzhskomr | ejxukcbau                                          | 19       | 4      |
| pdxafib                        | vcsfpqonshcrzowpcxptnjt                            | 18       | 3      |
| dcuzwcamcq                     | qjvzikdbxfhgtywyneozezwycafarobz                   | 9        | 1      |
| dcuzwcamcq                     | ojewashrlvl                                        | 18       | 4      |
| wrtmvtnx                       | zfzhyxlkrdrbkmbdpszcesblbcdtwornbwmb               | 18       | 5      |
| jgmsykrgxja                    | qbtrvwgmbzpaffixzuneosqrlbfnbqpjskogovgjm          | 14       | 4      |
| ebjfgw                         | zptzlgeklffhtgtjzoltkus                            | 7        | 3      |
| tlbaycikeiljhfvpwjzhdo         | gexjlwbjwwtbjefgwqkyeutbpxbdlpzib                  | 5        | 2      |
| yitrgpgc                       | bjpxstrvogvyvtywxukbf                              | 18       | 5      |
| ebjfgw                         | qwazvqcnjqmteguiriejle                             | 9        | 5      |
| drjghcpuulxohcihqoqwevt        | bdqvagkvmielufkudttjusttstdzdav                    | 11       | 1      |
| dcuzwcamcq                     | uprwkptagltwtmdqnlvuu                              | 12       | 2      |
| wrtmvtnx                       | ljuvfaju                                           | 9        | 3      |
| ekibmwgcor                     | mqxkhvnmrhbiqqchtnjgpidkppbrfws                    | 18       | 5      |
| iqvnelhdfrviaelkyjwywujr       | oljbtaygayjhgouvfzvcngtamwmjl                      | 14       | 3      |
| gqzldthnjzeclmapupzqeymvlv     | bxrugpnujjxefqkcqlteucjgowqaadxrebdqosrxayb        | 19       | 2      |
| uecqxryoivbnuo                 | xceenerldhggswuthyiuedgkxdlbwjazgzuym              | 12       | 4      |
| xfqiblw                        | ztftrhnglquujubfrhxeippwangireugtfaxqtv            | 5        | 4      |
| udrcvuaxzjhbnvcyo              | wnxkcarqhpqxzppjcxqwxe                             | 4        | 4      |
| udrcvuaxzjhbnvcyo              | mofniefpsnrsqkuxzespwomheagvgjdk                   | 8        | 5      |
| zpnqahfsebkahuxiwooptjga       | tngwcyyblyzlfyfxkxrgqwkbak                         | 20       | 1      |
| ryrujnbnciuzkpkypgoysyromxdvp  | rhbqphhrcrkos                                      | 13       | 1      |
| xfqiblw                        | mzvvmmvieqgifmouv                                  | 10       | 4      |
| fbceifhwyvgcwve                | zrauysnjmheavevrutqotncqrlspmsk                    | 14       | 3      |
| brlenjuadhbjaevowuwtfuoicgfey  | qzflaq                                             | 4        | 3      |
| kpeesbjqvadyizkbnxhbn          | xxoissjlzknoz                                      | 7        | 2      |
| uhbszpgzphqybjwgctapd          | qgmmfybfduwzxdjgvibvikmhvalwsyzqipnl               | 11       | 3      |
| duvrrsjdlqlmytfjjzulkar        | hnurzbqxzsrfxrnxxoxjshbrcxhxkfsofltikkmczqjsz      | 10       | 2      |
| wrtmvtnx                       | yrrqkatymgpxbenoaqjtuyz                            | 15       | 2      |
| haprwqoidtasctuzum             | prlbpcyhny                                         | 17       | 1      |
| inrbgu                         | vqjfcczzn                                          | 20       | 1      |
| fbceifhwyvgcwve                | yicgcpmpqpyfynphkfqmdojchkqnkdzyohtbwxgai          | 19       | 2      |
| dfyiagitstfpzycnojhfegbfcsmr   | sswogubqpgmsceutgpzkok                             | 14       | 5      |
| cfcwoydsmbcqds                 | zdxbshbziyb                                        | 1        | 5      |
| fzvkiv                         | gtbvvmlbebgwdioffutnuddfx                          | 4        | 5      |
| cjtxatphhnxwxkfjcojmvh         | esrzptxaqcgdovmwfdinfeavbltrm                      | 20       | 1      |
| gqzldthnjzeclmapupzqeymvlv     | ngyygihvpg                                         | 2        | 3      |
| niziwbxkmgjut                  | tofhtxdahuxgczhw                                   | 20       | 3      |
| xhbmfnz                        | ciggodvvsrnrkaclfeko                               | 17       | 3      |
| duvrrsjdlqlmytfjjzulkar        | twcciadqvrhmjozhfsqbbriscyplldrodwwhhwauqu         | 16       | 2      |
| ohwctqqdscnlxaqeqhcspxcb       | uwyroxgmwxfoknypwzpxiqijztjgxyiifiv                | 17       | 4      |
| vrdbnlmwbnrawopttryqkkfsjkx    | optdgjdnfgopzgu                                    | 18       | 4      |
| cfzjkoi                        | qhcycggfyceiyywtvabatni                            | 8        | 5      |
| boxmkivtcmaqgucfayepvdlrzkwstd | ezkylwoyddkvydagzrqswagjrz                         | 13       | 2      |
| ekibmwgcor                     | qvzudvvijmvdtjwr                                   | 19       | 3      |
| onjjde                         | czsfxbyxmyxpxylaefirtooqocrzkvbj                   | 19       | 3      |
| vxjmolnmove                    | hyfdvpuahrlkebqiqorramukpidysynggnqzrdbomtly       | 8        | 5      |
| duvrrsjdlqlmytfjjzulkar        | hzslwzkfkevfbucxgosaichtjeqz                       | 7        | 4      |
| oiunaci                        | grhuffqxgcboykovarbpzhh                            | 11       | 5      |
| stoomzsizgwpwguaikpdwwtczqt    | upwsrksbmbrwgjxxufsoptuasb                         | 19       | 2      |
| nvdrmuirylwyfvhqk              | zrjppzcmffnfaeumrhxdwqqhrorcmeikoavaprnqjfkgkeyjbz | 20       | 1      |
| uhbszpgzphqybjwgctapd          | rlvqmpuywshktxwkrdextmobysglsqefimizzatghqw        | 4        | 5      |
| hpzxmamailhqhipufrbhsbr        | tkeqzktylsvdocrteuhhoh                             | 15       | 3      |
| ryrujnbnciuzkpkypgoysyromxdvp  | cdokylpsibepzovilimtpyyemhnmevovcetehtzk           | 1        | 4      |
| pdxafib                        | hsmosukldcjabqgztbdmihidanpez                      | 14       | 3      |
| haprwqoidtasctuzum             | zjibgqbiffsfsubzzwdymnpeawdiivbng                  | 4        | 4      |
| ekibmwgcor                     | cxrkeinxjijngoobcwpkfprkckujgnp                    | 14       | 4      |
| mlcehcpuajedlk                 | kdjtrerodhnwmqdchixyzfcvrgmtkecs                   | 5        | 1      |
| udrcvuaxzjhbnvcyo              | xdkpzon                                            | 10       | 2      |
| fzjchf                         | pvwyrjgkvawwhrswodmoazzsbutdsvjfsmrcgft            | 3        | 5      |
| kpeesbjqvadyizkbnxhbn          | sleaqdrckztjsm                                     | 1        | 4      |
| oiunaci                        | bhywbidqmkprkdn                                    | 7        | 3      |
| qbaszrbkjiprliebfcju           | ffwftqmnsqedhjhkfqqnmktvddllaygqkodxkfuae          | 8        | 1      |
| onjjde                         | citvggoifvetbaainfdtwwgwbl                         | 12       | 4      |
| haprwqoidtasctuzum             | bweeqbdkkqllwppojqrnoazwq                          | 12       | 2      |
| pdxafib                        | dvqnboagdshqyjfsweulcwturycahxarllvurisduehl       | 4        | 3      |
| tlbaycikeiljhfvpwjzhdo         | snhnuxxqhlvvxvkptdspgkczeszegnwrmsedfxfqhxqjlikxcu | 10       | 2      |
| drjghcpuulxohcihqoqwevt        | afjvfujghthdwrultmwiotlfqxktlohgceedlwwukxgdwz     | 17       | 4      |
| duvrrsjdlqlmytfjjzulkar        | hzcurmtkazydrmiodlohyfcnsrsfzlosrgkpbmrzt          | 16       | 1      |
| jgmsykrgxja                    | mvyoocx                                            | 15       | 4      |
| tlbaycikeiljhfvpwjzhdo         | qnowcflshzeahmihgx                                 | 17       | 3      |
| mpzkxkzbompbpbavkb             | nhrqadcomwzniaewirrqjtykczj                        | 19       | 1      |
| stoomzsizgwpwguaikpdwwtczqt    | aqzcal                                             | 1        | 5      |
| fnxeqcpkjwbshszzlndo           | wzhfcpdpxeuqisagfqqt                               | 18       | 4      |
| fbceifhwyvgcwve                | ugdfg                                              | 6        | 4      |
| tlbaycikeiljhfvpwjzhdo         | hcdvlmwerxcnvklpwrveycuh                           | 2        | 3      |
| tfdmtfiegtqxixexmiqktspvonyw   | xarfczbknowogoefbimwbeuhtszsksrmqlvsjnvbwesprhr    | 11       | 4      |
| vrdbnlmwbnrawopttryqkkfsjkx    | bapjqqvvahtmarzzazxwajrv                           | 2        | 2      |
| yitrgpgc                       | jyoot                                              | 16       | 4      |
| niziwbxkmgjut                  | keujnqpmtfuecoeiadijwukiyrrqdjtvvssfldemkxb        | 8        | 5      |
| drjghcpuulxohcihqoqwevt        | tuzcyyhcmfkdevhyfsikzkeiczkqylcvhlguunbrojztvxei   | 17       | 4      |
| drjghcpuulxohcihqoqwevt        | zixvcoctqvgmlqdbomgmxmusfvqvsklyrveplvrytq         | 19       | 5      |
| xfqiblw                        | lotofkr                                            | 1        | 2      |
| xhbmfnz                        | bobvmishsrogcjekixzlskkfa                          | 5        | 5      |
| vrdbnlmwbnrawopttryqkkfsjkx    | zuyxnmfkjiddcfswlckufcy                            | 9        | 5      |
| tfdmtfiegtqxixexmiqktspvonyw   | zcgfpsvzjejckpvbllefsnvoobvqpwshagzdjvbhlor        | 19       | 3      |
| qbaszrbkjiprliebfcju           | eryisewxmoqxncoczgnzlr                             | 7        | 1      |
| boxmkivtcmaqgucfayepvdlrzkwstd | kxhlrefctkrnljlow                                  | 20       | 1      |
| cfcwoydsmbcqds                 | youwoectfftkzv                                     | 6        | 1      |
| udrcvuaxzjhbnvcyo              | jzosezpfmqxbpiefxx                                 | 14       | 3      |
| oiunaci                        | mddbnakdiuuaqwligxpkwzwojfecllbsoftx               | 9        | 2      |
| fzvkiv                         | rcqhrapdsaxcusn                                    | 18       | 5      |
| fbceifhwyvgcwve                | tmgnwwybcfijsbxalzzfrpzhch                         | 1        | 2      |
| cjtxatphhnxwxkfjcojmvh         | ofurwexpsbmkhciahdzxrbsjarptvevrf                  | 19       | 4      |
| haprwqoidtasctuzum             | lftigmbpwkulfbxh                                   | 7        | 1      |
| sjmpwulsgiiokkoxzmfrhfwjqegdf  | ktdramoljvbnbrlsldjsebhwwtlqogbtmlfffzlxhbbj       | 6        | 2      |
| skcyovx                        | owatjnwfcorrwlmhobfgffwaqw                         | 12       | 4      |
| stoomzsizgwpwguaikpdwwtczqt    | ngparrzjhdjoanukn                                  | 20       | 5      |
| fnxeqcpkjwbshszzlndo           | ocjvoxbrrpocalrzqivlqoeyfhmaq                      | 5        | 1      |
| udrcvuaxzjhbnvcyo              | wpiiorgtciyslxrvdravkawhnxzsgjazgkzeo              | 10       | 2      |
| tyrratimtbonzdwfsiurodhacx     | lvyqqioniusulfazrjucfzevujixq                      | 9        | 5      |
| vrdbnlmwbnrawopttryqkkfsjkx    | ulpwofbgphnljljvvsjf                               | 15       | 4      |
| ohwctqqdscnlxaqeqhcspxcb       | mlfuyvbjwha                                        | 3        | 5      |
| brlenjuadhbjaevowuwtfuoicgfey  | uztpoytpbeptlguxmxogwzho                           | 19       | 3      |
| wrtmvtnx                       | dwmtqisztucmjgmxebgrwcfntbcyxzxhwfmehviuklz        | 20       | 4      |
| ebjfgw                         | wpqpurllwnvpksovwvhinztsquubxjtl                   | 14       | 5      |
| xdyoviczumlpchsnsbnwqmljgh     | oaejcxgsqzvikhscdndwxczsdsbfbaffq                  | 17       | 3      |
| yitrgpgc                       | kqxyxxierauorxxlsjzcghuxpqnsexhpjacmlffqu          | 12       | 3      |
| duvrrsjdlqlmytfjjzulkar        | gfejetuvx                                          | 1        | 3      |
| haprwqoidtasctuzum             | xacznplvrtgrfcbvqzhjztnwwhusgpwzf                  | 11       | 5      |
| qbaszrbkjiprliebfcju           | zlfpmdr                                            | 5        | 5      |
| yitrgpgc                       | yubywazmliiyvlbueuoxvkihsaeiencsaiwpbrvipllcao     | 16       | 1      |
| xhbmfnz                        | ytsdedhlfbklcljnrmdouhubewfdazfsbvghfssmznhudt     | 15       | 5      |
| hpzxmamailhqhipufrbhsbr        | bsctvtffuobjuqpgfdovwjxxhwjmebvpjttzdlhbjscwbrlpn  | 18       | 3      |
| stoomzsizgwpwguaikpdwwtczqt    | evfrskqdggszvnmuawf                                | 2        | 5      |
| brlenjuadhbjaevowuwtfuoicgfey  | jyhycfoorqixtldvwxbcydpgkfxt                       | 8        | 3      |
| alprumqp                       | egumhioiusxzxgloooysobxpul                         | 15       | 1      |
| xdyoviczumlpchsnsbnwqmljgh     | fcjtuteubfhk                                       | 17       | 4      |
| glrqfhvwegnkw                  | sjhwjpleflhpzipbqjrsrwbgdplnzouvtqymglxjs          | 10       | 3      |
| cfzjkoi                        | zmpehsrnoubqqq                                     | 6        | 1      |
| jgmsykrgxja                    | rzdhgytloaill                                      | 20       | 4      |
| vbhbbbnntqiocpwf               | psolqvrbjtddypzwjlkpapjkfwbwkdmauknezyrexqorraxnc  | 17       | 3      |
| cfcwoydsmbcqds                 | bfeirhmfpxcyqamwmzndfkivvlphmdlbshwgydi            | 16       | 4      |
| dcuzwcamcq                     | ezrqbbfnwutuoqpqevyuyavx                           | 7        | 4      |
| szsgysmafhfhstnagzhryxykvkmzn  | ztoabulmvnqvoygndekztuvnxrpkw                      | 5        | 3      |
| snhrdtzetlihfenkdjyatadzhskomr | bgdgrbrlogqpgyteoihdchthefaaxgcnzl                 | 6        | 5      |
| brlenjuadhbjaevowuwtfuoicgfey  | wgzvyzbahiigpyktytmfigppuhuxlasvulqkknnolomtr      | 5        | 4      |
| pdxafib                        | bwlaihkijewqlqgpqjlgktsozzozeadirqworjq            | 11       | 3      |
| dfyiagitstfpzycnojhfegbfcsmr   | dzlbxmzgfmvusmvqdarglwrsolthmzjdowwcdgbowrsslhd    | 2        | 3      |
| wrtmvtnx                       | rbcvzyyechnazusrlvteevzmufbqozhlvcwxuudaseexrepv   | 3        | 2      |
| snhrdtzetlihfenkdjyatadzhskomr | pvnjfyrfa                                          | 20       | 1      |
| jgmsykrgxja                    | frqewbyohdc                                        | 16       | 5      |
| dcuzwcamcq                     | sozkdpbpqgluzxrncsbhpvrjqusyjh                     | 14       | 4      |
| snhrdtzetlihfenkdjyatadzhskomr | sabxwlnbupwkttowhcxpuhgbygk                        | 20       | 5      |
| iqvnelhdfrviaelkyjwywujr       | zozzpxvgphaisntnjbayhbexfhpzc                      | 3        | 1      |
| qbaszrbkjiprliebfcju           | ehvrbmubdt                                         | 12       | 4      |
| brlenjuadhbjaevowuwtfuoicgfey  | badgks                                             | 8        | 4      |
| alprumqp                       | rglqqqkgkjgiahewqhgtpxdanvuxbsjweaekvhcfchyrf      | 14       | 2      |
| jgmsykrgxja                    | kglcqddheoh                                        | 17       | 1      |
| inrbgu                         | iopwneccdrcnvcnoyhlaaiuxookahplqdxyaarxk           | 9        | 1      |
| yitrgpgc                       | qritjekq                                           | 11       | 1      |
| xhbmfnz                        | fjczcclqvewfa                                      | 16       | 2      |
| oiunaci                        | eqkpthxrrxclgoikdyuivmyugtinxzgofna                | 8        | 5      |
| vxjmolnmove                    | heylktdnntvgtevsorazrocmmkfjx                      | 11       | 1      |
| boxmkivtcmaqgucfayepvdlrzkwstd | wneeaeyuykx                                        | 15       | 4      |
| fnxeqcpkjwbshszzlndo           | lndgdovcxsufdpbzzzkynrykxboouxtnvqrrjjifuhqcan     | 1        | 3      |
| kpeesbjqvadyizkbnxhbn          | izflbqogfhmyo                                      | 11       | 4      |
| cfcwoydsmbcqds                 | ptlkkddzmzynkbectyojkaeun                          | 20       | 5      |
| vrdbnlmwbnrawopttryqkkfsjkx    | dcrsnngvqetqglczpuhpniwvfzmfxamvhyrqbfyrzxlbmpn    | 1        | 2      |
| ryrujnbnciuzkpkypgoysyromxdvp  | jwvjypxkhyxhijvzcbnvgo                             | 8        | 2      |
| snhrdtzetlihfenkdjyatadzhskomr | avnawsggwtmktmjbipmsrekvrfnkfvyijpnxwguqmccyzkxbn  | 4        | 3      |
| ejzvfzcid                      | cdrbpyykdzslkmsw                                   | 18       | 3      |
| dfyiagitstfpzycnojhfegbfcsmr   | ktqunreoln                                         | 13       | 3      |
| wrtmvtnx                       | pcpobiwegrenpnehqjqtiecuvbulrcprzkncyl             | 9        | 2      |
| oiunaci                        | tyawcuqkkjjclelusjjqjumcklxlaawiigi                | 9        | 2      |
| fzvkiv                         | wojqqhtqhmhgtukdqgmyfj                             | 10       | 4      |
| uecqxryoivbnuo                 | vcvxaxehgvttiskuinxupkzejppzieeizjyiybtkeqshfhkdq  | 7        | 1      |
| gqzldthnjzeclmapupzqeymvlv     | hmvyjekplfvntx                                     | 18       | 5      |
| ohwctqqdscnlxaqeqhcspxcb       | htjnrfnsbmjwqfjjaifiprlpkauvfhxorepnawyuenrpipuph  | 7        | 3      |
| yitrgpgc                       | zzoqbmbkynhrzwlqchbqxzigqeddcwpbbogswmbzabb        | 15       | 2      |
| vxjmolnmove                    | rxoepgdscwtfbulgmlxmvgrt                           | 10       | 4      |
| tfdmtfiegtqxixexmiqktspvonyw   | jocadzlesrytjuteiqkobvpdfsybgsnagetypcqdzewrtqs    | 3        | 5      |
| haprwqoidtasctuzum             | xnhiusrbwseaeyxzkjwxmbbgjclxlrgatiiribinlzhvqo     | 12       | 2      |
| onjjde                         | prybeglbxqeezmvjmxvvd                              | 5        | 1      |
| zaeoxboasertlctguemxos         | qgaewzkqzgnmskzlobdohayiaywchhgbchgtrqybfbpxmwldu  | 1        | 2      |
| inrbgu                         | lfzvotlrekybtolwneot                               | 8        | 2      |
| fnxeqcpkjwbshszzlndo           | wdjshhpuatlx                                       | 3        | 2      |
| cfzjkoi                        | novdfqyshwdultjklescpoytdorqdgmhpcmpilcvmzvnplndm  | 15       | 3      |
| unhozkflppkialzjsaaqjbdhsb     | hdesmsdmjpa                                        | 14       | 2      |
| ejzvfzcid                      | vnszqwwmqqfujfhitgcpljcylnt                        | 1        | 5      |
| xhbmfnz                        | svqittstzxhzbixnpslcivyjlaiixwfpwxchfmghyycoyh     | 20       | 1      |
| vbhbbbnntqiocpwf               | rclylk                                             | 2        | 1      |
| stoomzsizgwpwguaikpdwwtczqt    | tshllaliimqtvklrnbjyd                              | 10       | 4      |
| nvdrmuirylwyfvhqk              | zbheecekheklyynxvixplqo                            | 10       | 5      |
| fzvkiv                         | mqdelqwwkixrqhxsjypsfysmgpfwveirfnachjfjufnxvlva   | 18       | 3      |
| ebjfgw                         | dudchtthzwisetsqlrjrqbaqjwitc                      | 5        | 1      |
| tyrratimtbonzdwfsiurodhacx     | dafcwpujxvdvbnsciuzyodcahlnpxovnumis               | 13       | 4      |
| xfqiblw                        | hunkmmtgmtrhnflq                                   | 4        | 4      |
| gqzldthnjzeclmapupzqeymvlv     | ronefnnrjgwx                                       | 12       | 5      |
| vxjmolnmove                    | iscejbabvuzkglprplyqlqqvap                         | 10       | 5      |
| fzjchf                         | nbubdizxhpkhaolfydgbchrpdixahtcoao                 | 12       | 2      |
| nvdrmuirylwyfvhqk              | cfknnvnxyhauuqhheardfgvwrwcyqxcsfiwiauxnbeaukcuacr | 17       | 3      |
| szsgysmafhfhstnagzhryxykvkmzn  | jdarmblwlhnfmmsczajtqbfyfgxm                       | 20       | 1      |
| zaeoxboasertlctguemxos         | bwzbjqznrioxgosjfmvrnsdohycnwewrhk                 | 18       | 4      |
| brlenjuadhbjaevowuwtfuoicgfey  | bqcfbi                                             | 7        | 2      |
| ekibmwgcor                     | cpxulnsrrgyfkyectdzrztoyojubhizyaxemwukkdujt       | 13       | 2      |
| cfzjkoi                        | tbzuockmzmmdsismjfmopitkz                          | 3        | 1      |
| ebjfgw                         | nqgihmpeiawolizzcfxngz                             | 16       | 2      |
| qbaszrbkjiprliebfcju           | qqurli                                             | 9        | 4      |
| vrdbnlmwbnrawopttryqkkfsjkx    | mwscmfbgapuervupibgvxtzvnffqdvjrbvyxqanqlcwebe     | 13       | 1      |
| tyrratimtbonzdwfsiurodhacx     | mpvaoqensvcunqhwlwvxhzkjqxl                        | 14       | 5      |
| wwsrvtgndehtxtnnr              | vumjxanalxjbrxymrlpkrxriangfylkmsfdmyo             | 11       | 5      |
| inrbgu                         | haxtxtsjoadxgowitiahbpawlffijeqrvazkupcwwahdwq     | 6        | 4      |
| wwsrvtgndehtxtnnr              | rctoirlltonsrqvrepcjupkgtdhzdsjvcfk                | 10       | 4      |
| tfdmtfiegtqxixexmiqktspvonyw   | ymigsfynermhxzvdrqomwxaz                           | 20       | 4      |
| snhrdtzetlihfenkdjyatadzhskomr | zoqhuwmnckxytlhbgpfgwaucnffxexmuutxwjnowelgk       | 11       | 3      |
| vbhbbbnntqiocpwf               | acsnbksvtsj                                        | 4        | 3      |
| mlcehcpuajedlk                 | fplnidxbmfeazsidigmcgbuwxnuwfzp                    | 7        | 3      |
| zpnqahfsebkahuxiwooptjga       | ljqaggqyxqwmxmbtuilfcfomkhjlhqfveaegmdhs           | 3        | 5      |
| xhbmfnz                        | civcgrmdrkpvfdqzlfyocgnojtlxhiwiujhduhvgqjxmu      | 11       | 4      |
| unhozkflppkialzjsaaqjbdhsb     | ulbkobgkotkgaeuqivgrljulggaskjwxoxystwc            | 7        | 3      |
| drjghcpuulxohcihqoqwevt        | xfnwtiqsq                                          | 19       | 5      |
| ebjfgw                         | yhmcfhmbhslingmaxy                                 | 6        | 1      |
| xfqiblw                        | azicedfsqnkfwaeqczmwlrprsyybeagzykaooeax           | 3        | 5      |
| drjghcpuulxohcihqoqwevt        | vutgdljbkpoowyefxwadfyltkojfhdrt                   | 12       | 2      |
| fnxeqcpkjwbshszzlndo           | phecjkvpyhfkdsqmbbdhepdqiejjbeadfzq                | 7        | 5      |
| fzvkiv                         | bzolkkokmfptwj                                     | 13       | 4      |
| ejzvfzcid                      | kpldyegnsqus                                       | 11       | 4      |
| ebjfgw                         | ehyqtwutjmwmwr                                     | 12       | 3      |
| drjghcpuulxohcihqoqwevt        | pdkfhcanmgiuhxncf                                  | 7        | 3      |
| iqvnelhdfrviaelkyjwywujr       | slwwkbtddlhaqqvenqwuhlxkqiwscgfltbvlvkowf          | 4        | 4      |
| oiunaci                        | zmjlxmabislpjvlltnyy                               | 14       | 3      |
| alprumqp                       | xkbscoajsfkjxlidpkwoagtyjvgsbduhbfszrqskdneoboisj  | 11       | 2      |
| uhbszpgzphqybjwgctapd          | xalobzsvnfmrahpzuzszaqorjuchpoxbilnctijlojnms      | 2        | 2      |
| duvrrsjdlqlmytfjjzulkar        | ohetlbrkihbfihkxmqvcztiyslsjpdypwskfhjkwabx        | 15       | 5      |
| zaeoxboasertlctguemxos         | ratdz                                              | 19       | 3      |
| ejzvfzcid                      | ithegykpacleqcwwgzyewwlzavpogeaobzwon              | 4        | 4      |
| onjjde                         | qjsiqtvxlgl                                        | 20       | 2      |
| xfqiblw                        | qyrcutiekgt                                        | 14       | 3      |
| sjmpwulsgiiokkoxzmfrhfwjqegdf  | ntgtwcruryygcojrsbnrhfcfcu                         | 4        | 4      |
+--------------------------------+----------------------------------------------------+----------+--------+

'''
#query_df = pd.DataFrame({
#	'query_name': ['Dog', 'Dog', 'Dog', 'Cat', 'Cat', 'Cat'],
#	'result': ['Golden Retriever', 'German Shepherd', 'Mule', 'Shirazi', 'Siamese', 'Sphynx'],
#	'position': [1, 2, 200, 5, 3, 7],
#	'rating': [5, 5, 1, 2, 3, 4]
#})
query_df = pd.DataFrame({
	'query_name': ['udrcvuaxzjhbnvcyo', 'udrcvuaxzjhbnvcyo', 'zpnqahfsebkahuxiwooptjga', 'ryrujnbnciuzkpkypgoysyromxdvp', 'xfqiblw', 'fbceifhwyvgcwve', 'brlenjuadhbjaevowuwtfuoicgfey', 'kpeesbjqvadyizkbnxhbn', 'uhbszpgzphqybjwgctapd', 'duvrrsjdlqlmytfjjzulkar'],
	'result': ['wnxkcarqhpqxzppjcxqwxe', 'mofniefpsnrsqkuxzespwomheagvgjdk', 'tngwcyyblyzlfyfxkxrgqwkbak', 'rhbqphhrcrkos', 'mzvvmmvieqgifmouv', 'zrauysnjmheavevrutqotncqrlspmsk', 'qzflaq', 'xxoissjlzknoz', 'qgmmfybfduwzxdjgvibvikmhvalwsyzqipnl', 'hnurzbqxzsrfxrnxxoxjshbrcxhxkfsofltikkmczqjsz'],
	'position': [16, 10, 14, 3, 
	'rating': [4, 8, 20, 13, 10, 14, 4, 7, 11, 10]
})

query_df['quality'] = query_df['rating'] / query_df['position']
out_df = query_df.groupby('query_name').agg(
	quality=('quality', 'mean'),
#	poor_query_percentage=('quality', lambda r: r['rating'] / r['position'].count())
).round(2).reset_index()

#out_df['poor_query_percentage'] = query_df.groupby('query_name').apply(
#	lambda r: (r['rating'] < 3).sum() / r['position'].count()
#).reset_index(drop=True)
#out_df['poor_query_percentage'] = (out_df['poor_query_percentage'] * 100).round(2)
print(out_df)