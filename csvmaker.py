import csv
import re

data = """
12 temperament / 3 / 1.6291673878227053 per mil
12 temperament / 4 / 0.0 per mil
12 temperament / 5 / 11.405238445971133 per mil
12 temperament / 6 / 1.6291673878227053 per mil
12 temperament / 7 / 25.978411275729197 per mil
12 temperament / 8 / 0.0 per mil
12 temperament / 9 / 3.258334775645494 per mil
12 temperament / 10 / 11.405238445971133 per mil
12 temperament / 11 / 40.56838136270269 per mil
12 temperament / 12 / 1.6291673878227053 per mil
12 temperament / 13 / 33.77305147442555 per mil
12 temperament / 14 / 25.978411275729197 per mil
12 temperament / 15 / 9.776071058147927 per mil
12 temperament / 16 / 0.0 per mil
12 temperament / 17 / 4.129507917005768 per mil
12 temperament / 18 / 3.258334775645494 per mil
12 temperament / 5/3 / 13.034405833793784 per mil
12 temperament / 7/3 / 27.6075786635519 per mil
12 temperament / 11/3 / 41.135784582807645 per mil
12 temperament / 11/5 / 29.163142916731527 per mil
12 temperament / 13/3 / 32.143884086602334 per mil
12 temperament / 13/5 / 38.155043412936905 per mil
12 temperament / 13/9 / 30.514716698779807 per mil
12 temperament / 17/3 / 2.5003405291834646 per mil
12 temperament / 17/5 / 15.534746362976914 per mil
12 temperament / 17/9 / 0.8711731413604262 per mil

12 temperament avg: 25.3174561999479per mil

41 temperament / 3 / 0.4033529373804745 per mil
41 temperament / 4 / 0.0 per mil
41 temperament / 5 / 4.85492415565486 per mil
41 temperament / 6 / 0.4033529373804745 per mil
41 temperament / 7 / 2.4768732771163204 per mil
41 temperament / 8 / 0.0 per mil
41 temperament / 9 / 0.8067058747610323 per mil
41 temperament / 10 / 4.85492415565486 per mil
41 temperament / 11 / 3.9830155090441743 per mil
41 temperament / 12 / 0.4033529373804745 per mil
41 temperament / 13 / 6.877355029639487 per mil
41 temperament / 14 / 2.4768732771163204 per mil
41 temperament / 15 / 4.451571218274775 per mil
41 temperament / 16 / 0.0 per mil
41 temperament / 17 / 10.098134359417005 per mil
41 temperament / 18 / 0.8067058747610323 per mil
41 temperament / 5/3 / 5.258277093035502 per mil
41 temperament / 7/3 / 2.8802262144968784 per mil
41 temperament / 11/3 / 3.5796625716638664 per mil
41 temperament / 11/5 / 8.837939664699007 per mil
41 temperament / 13/3 / 6.4740020922594566 per mil
41 temperament / 13/5 / 11.732279185294626 per mil
41 temperament / 13/9 / 6.07064915487876 per mil
41 temperament / 17/3 / 9.694781422036058 per mil
41 temperament / 17/5 / 9.437185387367153 per mil
41 temperament / 17/9 / 9.291428484655917 per mil

41 temperament avg: 7.259598300873034per mil

53 temperament / 3 / 0.05684034379760394 per mil
53 temperament / 4 / 0.0 per mil
53 temperament / 5 / 1.173377906230122 per mil
53 temperament / 6 / 0.05684034379760394 per mil
53 temperament / 7 / 3.965832659377 per mil
53 temperament / 8 / 0.0 per mil
53 temperament / 9 / 0.11368068759518013 per mil
53 temperament / 10 / 1.173377906230122 per mil
53 temperament / 11 / 6.601429958052019 per mil
53 temperament / 12 / 0.05684034379760394 per mil
53 temperament / 13 / 2.326510593922415 per mil
53 temperament / 14 / 3.965832659377 per mil
53 temperament / 15 / 1.2302182500281145 per mil
53 temperament / 16 / 0.0 per mil
53 temperament / 17 / 6.876781391170344 per mil
53 temperament / 18 / 0.11368068759518013 per mil
53 temperament / 5/3 / 1.1165375624326845 per mil
53 temperament / 7/3 / 4.022673003174548 per mil
53 temperament / 11/3 / 6.544589614254193 per mil
53 temperament / 11/5 / 5.428052051821925 per mil
53 temperament / 13/3 / 2.2696702501243395 per mil
53 temperament / 13/5 / 1.1531326876920156 per mil
53 temperament / 13/9 / 2.212829906326985 per mil
53 temperament / 17/3 / 6.933621734967477 per mil
53 temperament / 17/5 / 8.050159297400494 per mil
53 temperament / 17/9 / 6.990462078765414 per mil

53 temperament avg: 4.527060744870649per mil

306 temperament / 3 / 0.004819540281864043 per mil
306 temperament / 4 / 0.0 per mil
306 temperament / 5 / 1.601316877343717 per mil
306 temperament / 6 / 0.004819540281864043 per mil
306 temperament / 7 / 0.16537957394402447 per mil
306 temperament / 8 / 0.0 per mil
306 temperament / 9 / 0.009639080563672575 per mil
306 temperament / 10 / 1.601316877343717 per mil
306 temperament / 11 / 1.3526950881928568 per mil
306 temperament / 12 / 0.004819540281864043 per mil
306 temperament / 13 / 1.0933129123340546 per mil
306 temperament / 14 / 0.16537957394402447 per mil
306 temperament / 15 / 1.6061364176250814 per mil
306 temperament / 16 / 0.0 per mil
306 temperament / 17 / 0.7724528673079684 per mil
306 temperament / 18 / 0.009639080563672575 per mil
306 temperament / 5/3 / 1.5964973370617974 per mil
306 temperament / 7/3 / 0.17019911422588851 per mil
306 temperament / 11/3 / 1.3478755479112703 per mil
306 temperament / 11/5 / 0.24862178915080468 per mil
306 temperament / 13/3 / 1.0981324526154053 per mil
306 temperament / 13/5 / 0.5733440665316447 per mil
306 temperament / 13/9 / 1.1029519928974496 per mil
306 temperament / 17/3 / 0.7676333270256741 per mil
306 temperament / 17/5 / 0.8288640100357902 per mil
306 temperament / 17/9 / 0.7628137867441431 per mil

306 temperament avg: 1.0555412746380157per mil

665 temperament / 3 / 9.470611850304067e-05 per mil
665 temperament / 4 / 0.0 per mil
665 temperament / 5 / 0.12358360916669975 per mil
665 temperament / 6 / 9.470611850304067e-05 per mil
665 temperament / 7 / 0.16387493487701743 per mil
665 temperament / 8 / 0.0 per mil
665 temperament / 9 / 0.0001894122369505702 per mil
665 temperament / 10 / 0.12358360916669975 per mil
665 temperament / 11 / 0.7187573025523308 per mil
665 temperament / 12 / 9.470611850304067e-05 per mil
665 temperament / 13 / 0.3121615581559434 per mil
665 temperament / 14 / 0.16387493487701743 per mil
665 temperament / 15 / 0.12367831528559137 per mil
665 temperament / 16 / 0.0 per mil
665 temperament / 17 / 0.2447961375571378 per mil
665 temperament / 18 / 0.0001894122369505702 per mil
665 temperament / 5/3 / 0.12348890304836324 per mil
665 temperament / 7/3 / 0.16396964099552047 per mil
665 temperament / 11/3 / 0.7188520086710559 per mil
665 temperament / 11/5 / 0.6614184867772266 per mil
665 temperament / 13/3 / 0.31225626427486275 per mil
665 temperament / 13/5 / 0.43574516732286517 per mil
665 temperament / 13/9 / 0.3123509703931715 per mil
665 temperament / 17/3 / 0.24470143143906498 per mil
665 temperament / 17/5 / 0.12121252839047969 per mil
665 temperament / 17/9 / 0.2446067253203399 per mil

665 temperament avg: 0.3320984669437999per mil

28 temperament / 3 / 13.533929292584679 per mil
28 temperament / 4 / 0.0 per mil
28 temperament / 5 / 0.49952345879072935 per mil
28 temperament / 6 / 13.533929292584679 per mil
28 temperament / 7 / 14.073649370967223 per mil
28 temperament / 8 / 0.0 per mil
28 temperament / 9 / 8.646427129116423 per mil
28 temperament / 10 / 0.49952345879072935 per mil
28 temperament / 11 / 4.8540956484169895 per mil
28 temperament / 12 / 13.533929292584679 per mil
28 temperament / 13 / 13.84599614462212 per mil
28 temperament / 14 / 14.073649370967223 per mil
28 temperament / 15 / 14.033452751375798 per mil
28 temperament / 16 / 0.0 per mil
28 temperament / 17 / 16.034269821767673 per mil
28 temperament / 18 / 8.646427129116423 per mil
28 temperament / 5/3 / 13.034405833793784 per mil
28 temperament / 7/3 / 8.106707050733824 per mil
28 temperament / 11/3 / 17.32626077328392 per mil
28 temperament / 11/5 / 5.353619107207718 per mil
28 temperament / 13/3 / 8.334360277078526 per mil
28 temperament / 13/5 / 14.34551960341307 per mil
28 temperament / 13/9 / 5.199569015505889 per mil
28 temperament / 17/3 / 2.5003405291834646 per mil
28 temperament / 17/5 / 15.534746362976914 per mil
28 temperament / 17/9 / 11.033588763401546 per mil

28 temperament avg: 14.786119967391503per mil

59 temperament / 3 / 8.257838261894745 per mil
59 temperament / 4 / 0.0 per mil
59 temperament / 5 / 0.10580341772253865 per mil
59 temperament / 6 / 8.257838261894745 per mil
59 temperament / 7 / 6.204399976294184 per mil
59 temperament / 8 / 0.0 per mil
59 temperament / 9 / 0.4334760185833453 per mil
59 temperament / 10 / 0.10580341772253865 per mil
59 temperament / 11 / 1.8044999932295136 per mil
59 temperament / 12 / 8.257838261894745 per mil
59 temperament / 13 / 5.524463903804011 per mil
59 temperament / 14 / 6.204399976294184 per mil
59 temperament / 15 / 8.363641679616896 per mil
59 temperament / 16 / 0.0 per mil
59 temperament / 17 / 2.717078538474693 per mil
59 temperament / 18 / 0.4334760185833453 per mil
59 temperament / 5/3 / 8.152034844172373 per mil
59 temperament / 7/3 / 2.0534382856006452 per mil
59 temperament / 11/3 / 6.886814287248799 per mil
59 temperament / 11/5 / 1.91030341095208 per mil
59 temperament / 13/3 / 3.16685037667451 per mil
59 temperament / 13/5 / 5.630267321526383 per mil
59 temperament / 13/9 / 5.090987885220444 per mil
59 temperament / 17/3 / 5.9742357420029535 per mil
59 temperament / 17/5 / 2.8228819561972873 per mil
59 temperament / 17/9 / 2.283602519891459 per mil

59 temperament avg: 6.290123397218528per mil

146 temperament / 3 / 2.770719899238272 per mil
146 temperament / 4 / 0.0 per mil
146 temperament / 5 / 0.010286668184089631 per mil
146 temperament / 6 / 2.770719899238272 per mil
146 temperament / 7 / 0.8642560245876174 per mil
146 temperament / 8 / 0.0 per mil
146 temperament / 9 / 1.3078752700166063 per mil
146 temperament / 10 / 0.010286668184089631 per mil
146 temperament / 11 / 0.5275090482562139 per mil
146 temperament / 12 / 2.770719899238272 per mil
146 temperament / 13 / 1.8095811547907958 per mil
146 temperament / 14 / 0.8642560245876174 per mil
146 temperament / 15 / 2.7810065674228612 per mil
146 temperament / 16 / 0.0 per mil
146 temperament / 17 / 1.5782546400718578 per mil
146 temperament / 18 / 1.3078752700166063 per mil
146 temperament / 5/3 / 2.760433231054016 per mil
146 temperament / 7/3 / 3.2143391446672887 per mil
146 temperament / 11/3 / 2.2432108509822246 per mil
146 temperament / 11/5 / 0.5172223800721243 per mil
146 temperament / 13/3 / 0.9611387444478925 per mil
146 temperament / 13/5 / 1.7992944866064842 per mil
146 temperament / 13/9 / 3.117456424807208 per mil
146 temperament / 17/3 / 2.5003405291834646 per mil
146 temperament / 17/5 / 1.5885413082559197 per mil
146 temperament / 17/9 / 0.27037937005514046 per mil

146 temperament avg: 2.3966064689978084per mil

643 temperament / 3 / 0.20355826392437493 per mil
643 temperament / 4 / 0.0 per mil
643 temperament / 5 / 0.0003654547839904154 per mil
643 temperament / 6 / 0.20355826392437493 per mil
643 temperament / 7 / 0.2009562722231628 per mil
643 temperament / 8 / 0.0 per mil
643 temperament / 9 / 0.40711652784869434 per mil
643 temperament / 10 / 0.0003654547839904154 per mil
643 temperament / 11 / 0.644682400905372 per mil
643 temperament / 12 / 0.20355826392437493 per mil
643 temperament / 13 / 0.5952391364265619 per mil
643 temperament / 14 / 0.2009562722231628 per mil
643 temperament / 15 / 0.2031928091408286 per mil
643 temperament / 16 / 0.0 per mil
643 temperament / 17 / 0.3710838630918145 per mil
643 temperament / 18 / 0.40711652784869434 per mil
643 temperament / 5/3 / 0.20392371870825432 per mil
643 temperament / 7/3 / 0.002601991701212114 per mil
643 temperament / 11/3 / 0.44112413698083053 per mil
643 temperament / 11/5 / 0.6450478556894179 per mil
643 temperament / 13/3 / 0.39168087250175676 per mil
643 temperament / 13/5 / 0.5956045912103303 per mil
643 temperament / 13/9 / 0.18812260857759 per mil
643 temperament / 17/3 / 0.16752559916788368 per mil
643 temperament / 17/5 / 0.37144931787580493 per mil
643 temperament / 17/9 / 0.03603266475682432 per mil

643 temperament avg: 0.41780392926370635per mil

4004 temperament / 3 / 0.04741580607114937 per mil
4004 temperament / 4 / 0.0 per mil
4004 temperament / 5 / 2.2959290246760133e-05 per mil
4004 temperament / 6 / 0.04741580607114937 per mil
4004 temperament / 7 / 0.08763538495326628 per mil
4004 temperament / 8 / 0.0 per mil
4004 temperament / 9 / 0.0948316121423265 per mil
4004 temperament / 10 / 2.2959290246760133e-05 per mil
4004 temperament / 11 / 0.10884090316221062 per mil
4004 temperament / 12 / 0.04741580607114937 per mil
4004 temperament / 13 / 0.10973240835832065 per mil
4004 temperament / 14 / 0.08763538495326628 per mil
4004 temperament / 15 / 0.04743876536184022 per mil
4004 temperament / 16 / 0.0 per mil
4004 temperament / 17 / 0.05025383775168757 per mil
4004 temperament / 18 / 0.0948316121423265 per mil
4004 temperament / 5/3 / 0.047392846780791587 per mil
4004 temperament / 7/3 / 0.11469905872582564 per mil
4004 temperament / 11/3 / 0.09349354051668701 per mil
4004 temperament / 11/5 / 0.10886386245248514 per mil
4004 temperament / 13/3 / 0.09260203532027167 per mil
4004 temperament / 13/5 / 0.10975536764884497 per mil
4004 temperament / 13/9 / 0.04518622924931659 per mil
4004 temperament / 17/3 / 0.002838031680996167 per mil
4004 temperament / 17/5 / 0.05023087846145469 per mil
4004 temperament / 17/9 / 0.04457777439048627 per mil

4004 temperament avg: 0.09582080442789662per mil

8651 temperament / 3 / 0.05657221838850646 per mil
8651 temperament / 4 / 0.0 per mil
8651 temperament / 5 / 5.91023346929731e-06 per mil
8651 temperament / 6 / 0.05657221838850646 per mil
8651 temperament / 7 / 0.04940824417221101 per mil
8651 temperament / 8 / 0.0 per mil
8651 temperament / 9 / 0.002449136220383785 per mil
8651 temperament / 10 / 5.91023346929731e-06 per mil
8651 temperament / 11 / 0.05283402713451846 per mil
8651 temperament / 12 / 0.05657221838850646 per mil
8651 temperament / 13 / 0.057334222796412426 per mil
8651 temperament / 14 / 0.04940824417221101 per mil
8651 temperament / 15 / 0.056578128621476154 per mil
8651 temperament / 16 / 0.0 per mil
8651 temperament / 17 / 0.04149350864830759 per mil
8651 temperament / 18 / 0.002449136220383785 per mil
8651 temperament / 5/3 / 0.05656630815509267 per mil
8651 temperament / 7/3 / 0.009613110436651473 per mil
8651 temperament / 11/3 / 0.0037381912537659545 per mil
8651 temperament / 11/5 / 0.052828116901076916 per mil
8651 temperament / 13/3 / 0.0007620044083500588 per mil
8651 temperament / 13/5 / 0.05732831256310966 per mil
8651 temperament / 13/9 / 0.05581021398037844 per mil
8651 temperament / 17/3 / 0.015078709740601326 per mil
8651 temperament / 17/5 / 0.04148759841482441 per mil
8651 temperament / 17/9 / 0.04394264486851096 per mil

8651 temperament avg: 0.051177395896295254per mil

12655 temperament / 3 / 0.023670752569704412 per mil
12655 temperament / 4 / 0.0 per mil
12655 temperament / 5 / 3.2239880209949945e-06 per mil
12655 temperament / 6 / 0.023670752569704412 per mil
12655 temperament / 7 / 0.0060480947436936106 per mil
12655 temperament / 8 / 0.0 per mil
12655 temperament / 9 / 0.03167864499883932 per mil
12655 temperament / 10 / 3.2239880209949945e-06 per mil
12655 temperament / 11 / 0.008465733306817214 per mil
12655 temperament / 12 / 0.023670752569704412 per mil
12655 temperament / 13 / 0.005107315331653872 per mil
12655 temperament / 14 / 0.0060480947436936106 per mil
12655 temperament / 15 / 0.02366752858129484 per mil
12655 temperament / 16 / 0.0 per mil
12655 temperament / 17 / 0.012464952742693991 per mil
12655 temperament / 18 / 0.03167864499883932 per mil
12655 temperament / 5/3 / 0.02367397655789194 per mil
12655 temperament / 7/3 / 0.029718847313370267 per mil
12655 temperament / 11/3 / 0.03213648587629958 per mil
12655 temperament / 11/5 / 0.008462509318768463 per mil
12655 temperament / 13/3 / 0.028778067900900317 per mil
12655 temperament / 13/5 / 0.0051040913433553214 per mil
12655 temperament / 13/9 / 0.02657132966743525 per mil
12655 temperament / 17/3 / 0.011205799827496143 per mil
12655 temperament / 17/5 / 0.012468176730728864 per mil
12655 temperament / 17/9 / 0.03487655239686749 per mil

12655 temperament avg: 0.025573347004112165per mil

26 temperament / 3 / 8.039423798079204 per mil
26 temperament / 4 / 0.0 per mil
26 temperament / 5 / 14.235787195054472 per mil
26 temperament / 6 / 8.039423798079204 per mil
26 temperament / 7 / 0.33738563470353533 per mil
26 temperament / 8 / 0.0 per mil
26 temperament / 9 / 16.078847596158298 per mil
26 temperament / 10 / 14.235787195054472 per mil
26 temperament / 11 / 2.106842901164252 per mil
26 temperament / 12 / 8.039423798079204 per mil
26 temperament / 13 / 8.132025833399892 per mil
26 temperament / 14 / 0.33738563470353533 per mil
26 temperament / 15 / 16.18632746840443 per mil
26 temperament / 16 / 0.0 per mil
26 temperament / 17 / 10.53976432726217 per mil
26 temperament / 18 / 16.078847596158298 per mil
26 temperament / 5/3 / 6.1963633969754905 per mil
26 temperament / 7/3 / 8.376809432782684 per mil
26 temperament / 11/3 / 10.146266699243567 per mil
26 temperament / 11/5 / 16.342630096218723 per mil
26 temperament / 13/3 / 0.09260203532027167 per mil
26 temperament / 13/5 / 6.103761361654858 per mil
26 temperament / 13/9 / 7.946821762758627 per mil
26 temperament / 17/3 / 2.5003405291834646 per mil
26 temperament / 17/5 / 3.696022867792359 per mil
26 temperament / 17/9 / 5.539083268896072 per mil

26 temperament avg: 11.832998389195442per mil

109 temperament / 3 / 2.1934625815962505 per mil
109 temperament / 4 / 0.0 per mil
109 temperament / 5 / 0.8271774561695033 per mil
109 temperament / 6 / 2.1934625815962505 per mil
109 temperament / 7 / 0.015472516319725571 per mil
109 temperament / 8 / 0.0 per mil
109 temperament / 9 / 4.386925163192446 per mil
109 temperament / 10 / 0.8271774561695033 per mil
109 temperament / 11 / 0.7160223070220573 per mil
109 temperament / 12 / 2.1934625815962505 per mil
109 temperament / 13 / 3.192011719073795 per mil
109 temperament / 14 / 0.015472516319725571 per mil
109 temperament / 15 / 1.3662851254262476 per mil
109 temperament / 16 / 0.0 per mil
109 temperament / 17 / 4.280278015715955 per mil
109 temperament / 18 / 4.386925163192446 per mil
109 temperament / 5/3 / 3.0206400377658094 per mil
109 temperament / 7/3 / 2.208935097915976 per mil
109 temperament / 11/3 / 2.9094848886180857 per mil
109 temperament / 11/5 / 0.11115514914744606 per mil
109 temperament / 13/3 / 3.7888376259359036 per mil
109 temperament / 13/5 / 2.3648342629040697 per mil
109 temperament / 13/9 / 1.5953750443394865 per mil
109 temperament / 17/3 / 2.08681543411926 per mil
109 temperament / 17/5 / 4.066856454720047 per mil
109 temperament / 17/9 / 0.10664714747654624 per mil

109 temperament avg: 3.0533572703957983per mil

571 temperament / 3 / 0.023796693135014202 per mil
571 temperament / 4 / 0.0 per mil
571 temperament / 5 / 0.3135863735835298 per mil
571 temperament / 6 / 0.023796693135014202 per mil
571 temperament / 7 / 0.0005945798738915542 per mil
571 temperament / 8 / 0.0 per mil
571 temperament / 9 / 0.04759338627011167 per mil
571 temperament / 10 / 0.3135863735835298 per mil
571 temperament / 11 / 0.5874855374724541 per mil
571 temperament / 12 / 0.023796693135014202 per mil
571 temperament / 13 / 0.08567590444197304 per mil
571 temperament / 14 / 0.0005945798738915542 per mil
571 temperament / 15 / 0.289789680448016 per mil
571 temperament / 16 / 0.0 per mil
571 temperament / 17 / 0.10283300535267326 per mil
571 temperament / 18 / 0.04759338627011167 per mil
571 temperament / 5/3 / 0.3373830667184885 per mil
571 temperament / 7/3 / 0.024391273008989023 per mil
571 temperament / 11/3 / 0.5636888443371069 per mil
571 temperament / 11/5 / 0.8502415740578584 per mil
571 temperament / 13/3 / 0.10947259757747296 per mil
571 temperament / 13/5 / 0.22791046914133473 per mil
571 temperament / 13/9 / 0.1332692907123345 per mil
571 temperament / 17/3 / 0.12662969848731276 per mil
571 temperament / 17/5 / 0.21075336823084267 per mil
571 temperament / 17/9 / 0.15042639162266003 per mil

571 temperament avg: 0.28718059127935164per mil

2393 temperament / 3 / 0.07719840128439515 per mil
2393 temperament / 4 / 0.0 per mil
2393 temperament / 5 / 0.15626037001992277 per mil
2393 temperament / 6 / 0.07719840128439515 per mil
2393 temperament / 7 / 0.00013726863634655473 per mil
2393 temperament / 8 / 0.0 per mil
2393 temperament / 9 / 0.15439680256876254 per mil
2393 temperament / 10 / 0.15626037001992277 per mil
2393 temperament / 11 / 0.1754548261815314 per mil
2393 temperament / 12 / 0.07719840128439515 per mil
2393 temperament / 13 / 0.06362119165637115 per mil
2393 temperament / 14 / 0.00013726863634655473 per mil
2393 temperament / 15 / 0.07906196873597171 per mil
2393 temperament / 16 / 0.0 per mil
2393 temperament / 17 / 0.1247718813462001 per mil
2393 temperament / 18 / 0.15439680256876254 per mil
2393 temperament / 5/3 / 0.18442672806873173 per mil
2393 temperament / 7/3 / 0.07733566992071395 per mil
2393 temperament / 11/3 / 0.16523227190745615 per mil
2393 temperament / 11/5 / 0.019194456161636397 per mil
2393 temperament / 13/3 / 0.1408195929402528 per mil
2393 temperament / 13/5 / 0.09263917836382918 per mil
2393 temperament / 13/9 / 0.1998675051483323 per mil
2393 temperament / 17/3 / 0.20197028263102546 per mil
2393 temperament / 17/5 / 0.03148848867373655 per mil
2393 temperament / 17/9 / 0.13871681545807313 per mil

2393 temperament avg: 0.15923655896856945per mil

2964 temperament / 3 / 0.0577421938237066 per mil
2964 temperament / 4 / 0.0 per mil
2964 temperament / 5 / 0.06574670922454562 per mil
2964 temperament / 6 / 0.0577421938237066 per mil
2964 temperament / 7 / 3.718374275152314e-06 per mil
2964 temperament / 8 / 0.0 per mil
2964 temperament / 9 / 0.11548438764735769 per mil
2964 temperament / 10 / 0.06574670922454562 per mil
2964 temperament / 11 / 0.08255140318852439 per mil
2964 temperament / 12 / 0.0577421938237066 per mil
2964 temperament / 13 / 0.034859841497092425 per mil
2964 temperament / 14 / 3.718374275152314e-06 per mil
2964 temperament / 15 / 0.008004515401283108 per mil
2964 temperament / 16 / 0.0 per mil
2964 temperament / 17 / 0.08092492105434002 per mil
2964 temperament / 18 / 0.11548438764735769 per mil
2964 temperament / 5/3 / 0.12348890304836324 per mil
2964 temperament / 7/3 / 0.0577384754494592 per mil
2964 temperament / 11/3 / 0.02480920936509534 per mil
2964 temperament / 11/5 / 0.14829811241304225 per mil
2964 temperament / 13/3 / 0.09260203532027167 per mil
2964 temperament / 13/5 / 0.03088686772773075 per mil
2964 temperament / 13/9 / 0.15034422914417256 per mil
2964 temperament / 17/3 / 0.13866711487842132 per mil
2964 temperament / 17/5 / 0.01517821182983603 per mil
2964 temperament / 17/9 / 0.14097260762746533 per mil

2964 temperament avg: 0.10406391624428589per mil

88349 temperament / 3 / 0.0016754438260102589 per mil
88349 temperament / 4 / 0.0 per mil
88349 temperament / 5 / 0.0002858572656361247 per mil
88349 temperament / 6 / 0.0016754438260102589 per mil
88349 temperament / 7 / 1.003663818721634e-07 per mil
88349 temperament / 8 / 0.0 per mil
88349 temperament / 9 / 0.0033508876519650066 per mil
88349 temperament / 10 / 0.0002858572656361247 per mil
88349 temperament / 11 / 0.003668122860234213 per mil
88349 temperament / 12 / 0.0016754438260102589 per mil
88349 temperament / 13 / 0.0016826228633748386 per mil
88349 temperament / 14 / 1.003663818721634e-07 per mil
88349 temperament / 15 / 0.001389586559930045 per mil
88349 temperament / 16 / 0.0 per mil
88349 temperament / 17 / 0.002881318704323066 per mil
88349 temperament / 18 / 0.0033508876519650066 per mil
88349 temperament / 5/3 / 0.001961301091757406 per mil
88349 temperament / 7/3 / 0.001675544192392131 per mil
88349 temperament / 11/3 / 0.005343566686022427 per mil
88349 temperament / 11/5 / 0.003382265594625844 per mil
88349 temperament / 13/3 / 0.003358066688885497 per mil
88349 temperament / 13/5 / 0.0013967655974611581 per mil
88349 temperament / 13/9 / 0.005033510515062289 per mil
88349 temperament / 17/3 / 0.004556762530749658 per mil
88349 temperament / 17/5 / 0.0025954614386591857 per mil
88349 temperament / 17/9 / 0.005086540884602364 per mil

88349 temperament avg: 0.0035194661408798067per mil

11 temperament / 3 / 39.507955266610665 per mil
11 temperament / 4 / 0.0 per mil
11 temperament / 5 / 41.70826874900146 per mil
11 temperament / 6 / 39.507955266610665 per mil
11 temperament / 7 / 10.82689612421406 per mil
11 temperament / 8 / 0.0 per mil
11 temperament / 9 / 11.893180375869672 per mil
11 temperament / 10 / 41.70826874900146 per mil
11 temperament / 11 / 4.886164091842781 per mil
11 temperament / 12 / 39.507955266610665 per mil
11 temperament / 13 / 26.83300913163511 per mil
11 temperament / 14 / 10.82689612421406 per mil
11 temperament / 15 / 2.200313482390359 per mil
11 temperament / 16 / 0.0 per mil
11 temperament / 17 / 3.4462496587518157 per mil
11 temperament / 18 / 11.893180375869672 per mil
11 temperament / 5/3 / 9.692866893478925 per mil
11 temperament / 7/3 / 40.574239518266275 per mil
11 temperament / 11/3 / 34.62179117476805 per mil
11 temperament / 11/5 / 44.31465806824669 per mil
11 temperament / 13/3 / 24.568126510844753 per mil
11 temperament / 13/5 / 14.875259617366133 per mil
11 temperament / 13/9 / 14.939828755765605 per mil
11 temperament / 17/3 / 42.95420492536195 per mil
11 temperament / 17/5 / 38.26201909024962 per mil
11 temperament / 17/9 / 8.446930717117995 per mil

11 temperament avg: 34.87476362088053per mil

13 temperament / 3 / 30.422114663459343 per mil
13 temperament / 4 / 0.0 per mil
13 temperament / 5 / 14.235787195054472 per mil
13 temperament / 6 / 30.422114663459343 per mil
13 temperament / 7 / 38.1241528268349 per mil
13 temperament / 8 / 0.0 per mil
13 temperament / 9 / 16.078847596158298 per mil
13 temperament / 10 / 14.235787195054472 per mil
13 temperament / 11 / 2.106842901164252 per mil
13 temperament / 12 / 30.422114663459343 per mil
13 temperament / 13 / 8.132025833399892 per mil
13 temperament / 14 / 38.1241528268349 per mil
13 temperament / 15 / 16.18632746840443 per mil
13 temperament / 16 / 0.0 per mil
13 temperament / 17 / 10.53976432726217 per mil
13 temperament / 18 / 16.078847596158298 per mil
13 temperament / 5/3 / 32.26517506456305 per mil
13 temperament / 7/3 / 8.376809432782684 per mil
13 temperament / 11/3 / 28.31527176229487 per mil
13 temperament / 11/5 / 16.342630096218723 per mil
13 temperament / 13/3 / 38.36893642621819 per mil
13 temperament / 13/5 / 6.103761361654858 per mil
13 temperament / 13/9 / 7.946821762758627 per mil
13 temperament / 17/3 / 35.96119793235497 per mil
13 temperament / 17/5 / 3.696022867792359 per mil
13 temperament / 17/9 / 5.539083268896072 per mil

13 temperament avg: 28.00153685826491per mil

24 temperament / 3 / 1.6291673878227053 per mil
24 temperament / 4 / 0.0 per mil
24 temperament / 5 / 11.405238445971133 per mil
24 temperament / 6 / 1.6291673878227053 per mil
24 temperament / 7 / 15.688255390937545 per mil
24 temperament / 8 / 0.0 per mil
24 temperament / 9 / 3.258334775645494 per mil
24 temperament / 10 / 11.405238445971133 per mil
24 temperament / 11 / 1.0982853039639973 per mil
24 temperament / 12 / 1.6291673878227053 per mil
24 temperament / 13 / 7.893615192241188 per mil
24 temperament / 14 / 15.688255390937545 per mil
24 temperament / 15 / 9.776071058147927 per mil
24 temperament / 16 / 0.0 per mil
24 temperament / 17 / 4.129507917005768 per mil
24 temperament / 18 / 3.258334775645494 per mil
24 temperament / 5/3 / 13.034405833793784 per mil
24 temperament / 7/3 / 14.059088003114756 per mil
24 temperament / 11/3 / 0.5308820838589856 per mil
24 temperament / 11/5 / 12.50352374993513 per mil
24 temperament / 13/3 / 9.522782580064337 per mil
24 temperament / 13/5 / 3.5116232537297787 per mil
24 temperament / 13/9 / 11.151949967886821 per mil
24 temperament / 17/3 / 2.5003405291834646 per mil
24 temperament / 17/5 / 15.534746362976914 per mil
24 temperament / 17/9 / 0.8711731413604262 per mil

24 temperament avg: 10.731822147864982per mil

37 temperament / 3 / 9.632093873438553 per mil
37 temperament / 4 / 0.0 per mil
37 temperament / 5 / 2.3962294369621606 per mil
37 temperament / 6 / 9.632093873438553 per mil
37 temperament / 7 / 3.4558887532066818 per mil
37 temperament / 8 / 0.0 per mil
37 temperament / 9 / 7.76283928014998 per mil
37 temperament / 10 / 2.3962294369621606 per mil
37 temperament / 11 / 0.027840822162172874 per mil
37 temperament / 12 / 9.632093873438553 per mil
37 temperament / 13 / 2.2629845616105593 per mil
37 temperament / 14 / 3.4558887532066818 per mil
37 temperament / 15 / 12.028323310400268 per mil
37 temperament / 16 / 0.0 per mil
37 temperament / 17 / 6.38176016925801 per mil
37 temperament / 18 / 7.76283928014998 per mil
37 temperament / 5/3 / 7.235864436476502 per mil
37 temperament / 7/3 / 6.17620512023187 per mil
37 temperament / 11/3 / 9.604253051276102 per mil
37 temperament / 11/5 / 2.3683886147999877 per mil
37 temperament / 13/3 / 7.369109311827549 per mil
37 temperament / 13/5 / 0.1332448753513793 per mil
37 temperament / 13/9 / 10.025823841760761 per mil
37 temperament / 17/3 / 11.013172984330023 per mil
37 temperament / 17/5 / 8.777989606220116 per mil
37 temperament / 17/9 / 1.381079110891914 per mil

37 temperament avg: 8.807014773596904per mil

949 temperament / 3 / 0.1363679498178616 per mil
949 temperament / 4 / 0.0 per mil
949 temperament / 5 / 0.5165837216999924 per mil
949 temperament / 6 / 0.1363679498178616 per mil
949 temperament / 7 / 0.18948475518054675 per mil
949 temperament / 8 / 0.0 per mil
949 temperament / 9 / 0.27273589963563993 per mil
949 temperament / 10 / 0.5165837216999924 per mil
949 temperament / 11 / 0.0006386583721318395 per mil
949 temperament / 12 / 0.1363679498178616 per mil
949 temperament / 13 / 0.2979004047455325 per mil
949 temperament / 14 / 0.18948475518054675 per mil
949 temperament / 15 / 0.38021577188174227 per mil
949 temperament / 16 / 0.0 per mil
949 temperament / 17 / 0.0023565295804023334 per mil
949 temperament / 18 / 0.27273589963563993 per mil
949 temperament / 5/3 / 0.40078910825047664 per mil
949 temperament / 7/3 / 0.05311680536274066 per mil
949 temperament / 11/3 / 0.1357292914458963 per mil
949 temperament / 11/5 / 0.5172223800721243 per mil
949 temperament / 13/3 / 0.4342683545638104 per mil
949 temperament / 13/5 / 0.21868331695423793 per mil
949 temperament / 13/9 / 0.48310447538679746 per mil
949 temperament / 17/3 / 0.1340114202369458 per mil
949 temperament / 17/5 / 0.5189402512804087 per mil
949 temperament / 17/9 / 0.27037937005514046 per mil

949 temperament avg: 0.3883792962921457per mil

986 temperament / 3 / 0.2301970476066284 per mil
986 temperament / 4 / 0.0 per mil
986 temperament / 5 / 0.42708068857921777 per mil
986 temperament / 6 / 0.2301970476066284 per mil
986 temperament / 7 / 0.0526908202816978 per mil
986 temperament / 8 / 0.0 per mil
986 temperament / 9 / 0.4603940952132013 per mil
986 temperament / 10 / 0.42708068857921777 per mil
986 temperament / 11 / 0.00043004424427062204 per mil
986 temperament / 12 / 0.2301970476066284 per mil
986 temperament / 13 / 0.37164088527696926 per mil
986 temperament / 14 / 0.0526908202816978 per mil
986 temperament / 15 / 0.19688364097303346 per mil
986 temperament / 16 / 0.0 per mil
986 temperament / 17 / 0.241745915653499 per mil
986 temperament / 18 / 0.4603940952132013 per mil
986 temperament / 5/3 / 0.35692104677553793 per mil
986 temperament / 7/3 / 0.2828878678882707 per mil
986 temperament / 11/3 / 0.22976700336208022 per mil
986 temperament / 11/5 / 0.4275107328234884 per mil
986 temperament / 13/3 / 0.14144383767082658 per mil
986 temperament / 13/5 / 0.21547720910503054 per mil
986 temperament / 13/9 / 0.08875320993595448 per mil
986 temperament / 17/3 / 0.4719429632605854 per mil
986 temperament / 17/5 / 0.18533477292570488 per mil
986 temperament / 17/9 / 0.3120587720946144 per mil

986 temperament avg: 0.38085751580987404per mil

1935 temperament / 3 / 0.0504191754847616 per mil
1935 temperament / 4 / 0.0 per mil
1935 temperament / 5 / 0.03572940204349395 per mil
1935 temperament / 6 / 0.0504191754847616 per mil
1935 temperament / 7 / 0.11977993874112691 per mil
1935 temperament / 8 / 0.0 per mil
1935 temperament / 9 / 0.10083835096949545 per mil
1935 temperament / 10 / 0.03572940204349395 per mil
1935 temperament / 11 / 9.408949369626995e-05 per mil
1935 temperament / 12 / 0.0504191754847616 per mil
1935 temperament / 13 / 0.1813202082756593 per mil
1935 temperament / 14 / 0.11977993874112691 per mil
1935 temperament / 15 / 0.08614857752775595 per mil
1935 temperament / 16 / 0.0 per mil
1935 temperament / 17 / 0.12433995834942868 per mil
1935 temperament / 18 / 0.10083835096949545 per mil
1935 temperament / 5/3 / 0.014689773441323162 per mil
1935 temperament / 7/3 / 0.17019911422588851 per mil
1935 temperament / 11/3 / 0.05051326497818032 per mil
1935 temperament / 11/5 / 0.03582349153719022 per mil
1935 temperament / 13/3 / 0.23173938375994907 per mil
1935 temperament / 13/5 / 0.21704961031893122 per mil
1935 temperament / 13/9 / 0.2346373063881746 per mil
1935 temperament / 17/3 / 0.17475913383457886 per mil
1935 temperament / 17/5 / 0.16006936039292263 per mil
1935 temperament / 17/9 / 0.2251783093190074 per mil

1935 temperament avg: 0.16065715573782524per mil

10 temperament / 3 / 15.037499278843903 per mil
10 temperament / 4 / 0.0 per mil
10 temperament / 5 / 21.928094887362192 per mil
10 temperament / 6 / 15.037499278843903 per mil
10 temperament / 7 / 7.35492205760413 per mil
10 temperament / 8 / 0.0 per mil
10 temperament / 9 / 30.07499855768786 per mil
10 temperament / 10 / 21.928094887362192 per mil
10 temperament / 11 / 40.56838136270269 per mil
10 temperament / 12 / 15.037499278843903 per mil
10 temperament / 13 / 0.43971814109222684 per mil
10 temperament / 14 / 7.35492205760413 per mil
10 temperament / 15 / 6.890595608518679 per mil
10 temperament / 16 / 0.0 per mil
10 temperament / 17 / 12.53715874966091 per mil
10 temperament / 18 / 30.07499855768786 per mil
10 temperament / 5/3 / 36.96559416620626 per mil
10 temperament / 7/3 / 22.392421336448088 per mil
10 temperament / 11/3 / 25.53088208385901 per mil
10 temperament / 11/5 / 37.50352374993513 per mil
10 temperament / 13/3 / 15.477217419935657 per mil
10 temperament / 13/5 / 21.488376746270244 per mil
10 temperament / 13/9 / 30.514716698779807 per mil
10 temperament / 17/3 / 2.5003405291834646 per mil
10 temperament / 17/5 / 34.46525363702313 per mil
10 temperament / 17/9 / 17.537839808027034 per mil

10 temperament avg: 29.29003430496765per mil

227 temperament / 3 / 0.9405829792844544 per mil
227 temperament / 4 / 0.0 per mil
227 temperament / 5 / 0.34219180366173996 per mil
227 temperament / 6 / 0.9405829792844544 per mil
227 temperament / 7 / 1.1875211765468574 per mil
227 temperament / 8 / 0.0 per mil
227 temperament / 9 / 1.881165958568909 per mil
227 temperament / 10 / 0.34219180366173996 per mil
227 temperament / 11 / 1.2818389016144849 per mil
227 temperament / 12 / 0.9405829792844544 per mil
227 temperament / 13 / 0.0008104932690544686 per mil
227 temperament / 14 / 1.1875211765468574 per mil
227 temperament / 15 / 0.5983911756222149 per mil
227 temperament / 16 / 0.0 per mil
227 temperament / 17 / 0.6428856219076046 per mil
227 temperament / 18 / 1.881165958568909 per mil
227 temperament / 5/3 / 1.28277478294625 per mil
227 temperament / 7/3 / 2.1281041558313674 per mil
227 temperament / 11/3 / 2.1828644627136518 per mil
227 temperament / 11/5 / 0.9396470979527449 per mil
227 temperament / 13/3 / 0.9397724860149559 per mil
227 temperament / 13/5 / 0.34300229693101647 per mil
227 temperament / 13/9 / 1.8803554652996324 per mil
227 temperament / 17/3 / 0.2976973573772801 per mil
227 temperament / 17/5 / 0.9850774255693029 per mil
227 temperament / 17/9 / 1.2382803366614015 per mil

227 temperament avg: 1.5240630546949585per mil

5231 temperament / 3 / 0.011691593888807361 per mil
5231 temperament / 4 / 0.0 per mil
5231 temperament / 5 / 0.0011210773832037724 per mil
5231 temperament / 6 / 0.011691593888807361 per mil
5231 temperament / 7 / 0.05230305550130154 per mil
5231 temperament / 8 / 0.0 per mil
5231 temperament / 9 / 0.02338318777769799 per mil
5231 temperament / 10 / 0.0011210773832037724 per mil
5231 temperament / 11 / 0.05482643695320366 per mil
5231 temperament / 12 / 0.011691593888807361 per mil
5231 temperament / 13 / 3.165667239457548e-05 per mil
5231 temperament / 14 / 0.05230305550130154 per mil
5231 temperament / 15 / 0.01057051650521501 per mil
5231 temperament / 16 / 0.0 per mil
5231 temperament / 17 / 0.0921195602133773 per mil
5231 temperament / 18 / 0.02338318777769799 per mil
5231 temperament / 5/3 / 0.012812671272177667 per mil
5231 temperament / 7/3 / 0.06399464939016442 per mil
5231 temperament / 11/3 / 0.06651803084178898 per mil
5231 temperament / 11/5 / 0.05370535956999989 per mil
5231 temperament / 13/3 / 0.011723250560785603 per mil
5231 temperament / 13/5 / 0.0010894207110312415 per mil
5231 temperament / 13/9 / 0.023414844449898276 per mil
5231 temperament / 17/3 / 0.08042796632412585 per mil
5231 temperament / 17/5 / 0.09324063759663659 per mil
5231 temperament / 17/9 / 0.06873637243554054 per mil

5231 temperament avg: 0.05136879978044802per mil

5458 temperament / 3 / 0.05032448954378488 per mil
5458 temperament / 4 / 0.0 per mil
5458 temperament / 5 / 0.015306320121422079 per mil
5458 temperament / 6 / 0.05032448954378488 per mil
5458 temperament / 7 / 0.08370014833203321 per mil
5458 temperament / 8 / 0.0 per mil
5458 temperament / 9 / 0.08256831662509234 per mil
5458 temperament / 10 / 0.015306320121422079 per mil
5458 temperament / 11 / 0.07735901019262359 per mil
5458 temperament / 12 / 0.05032448954378488 per mil
5458 temperament / 13 / 3.3686183842362993e-06 per mil
5458 temperament / 14 / 0.08370014833203321 per mil
5458 temperament / 15 / 0.03501816942197422 per mil
5458 temperament / 16 / 0.0 per mil
5458 temperament / 17 / 0.06819119537390672 per mil
5458 temperament / 18 / 0.08256831662509234 per mil
5458 temperament / 5/3 / 0.06563080966537349 per mil
5458 temperament / 7/3 / 0.03337565878824833 per mil
5458 temperament / 11/3 / 0.027034520649005245 per mil
5458 temperament / 11/5 / 0.09055196539867194 per mil
5458 temperament / 13/3 / 0.05032112092503982 per mil
5458 temperament / 13/5 / 0.015309688739972849 per mil
5458 temperament / 13/9 / 0.08257168524361536 per mil
5458 temperament / 17/3 / 0.06470161079452641 per mil
5458 temperament / 17/5 / 0.05288487525245689 per mil
5458 temperament / 17/9 / 0.014377121251074598 per mil

5458 temperament avg: 0.07446586494395772per mil

54353 temperament / 3 / 0.008588333615389132 per mil
54353 temperament / 4 / 0.0 per mil
54353 temperament / 5 / 0.004457133685409342 per mil
54353 temperament / 6 / 0.008588333615389132 per mil
54353 temperament / 7 / 0.0029819623011961838 per mil
54353 temperament / 8 / 0.0 per mil
54353 temperament / 9 / 0.0012215812560112393 per mil
54353 temperament / 10 / 0.004457133685409342 per mil
54353 temperament / 11 / 0.008955674811350622 per mil
54353 temperament / 12 / 0.008588333615389132 per mil
54353 temperament / 13 / 2.258970788204806e-09 per mil
54353 temperament / 14 / 0.0029819623011961838 per mil
54353 temperament / 15 / 0.004131199930368368 per mil
54353 temperament / 16 / 0.0 per mil
54353 temperament / 17 / 0.002432055642168085 per mil
54353 temperament / 18 / 0.0012215812560112393 per mil
54353 temperament / 5/3 / 0.005352781186074296 per mil
54353 temperament / 7/3 / 0.005606371314109682 per mil
54353 temperament / 11/3 / 0.00036734119579495683 per mil
54353 temperament / 11/5 / 0.004985439990001783 per mil
54353 temperament / 13/3 / 0.0085883313568208 per mil
54353 temperament / 13/5 / 0.004457135944213597 per mil
54353 temperament / 13/9 / 0.0012215835147877385 per mil
54353 temperament / 17/3 / 0.007377859229662498 per mil
54353 temperament / 17/5 / 0.002025078043255135 per mil
54353 temperament / 17/9 / 0.0012104743860597011 per mil

54353 temperament avg: 0.006237355258439936per mil

23 temperament / 3 / 19.745109416808294 per mil
23 temperament / 4 / 0.0 per mil
23 temperament / 5 / 17.58026880040564 per mil
23 temperament / 6 / 19.745109416808294 per mil
23 temperament / 7 / 18.732034464134962 per mil
23 temperament / 8 / 0.0 per mil
23 temperament / 9 / 3.9880420359487134 per mil
23 temperament / 10 / 17.58026880040564 per mil
23 temperament / 11 / 18.829250927920093 per mil
23 temperament / 12 / 19.745109416808294 per mil
23 temperament / 13 / 4.7875442280487235 per mil
23 temperament / 14 / 18.732034464134962 per mil
23 temperament / 15 / 6.152882652350811 per mil
23 temperament / 16 / 0.0 per mil
23 temperament / 17 / 0.5063195112086638 per mil
23 temperament / 18 / 3.9880420359487134 per mil
23 temperament / 5/3 / 2.1648406164024303 per mil
23 temperament / 7/3 / 5.001116988622018 per mil
23 temperament / 11/3 / 4.903900524836691 per mil
23 temperament / 11/5 / 7.068741141239482 per mil
23 temperament / 13/3 / 14.957565188759986 per mil
23 temperament / 13/5 / 12.792724572357194 per mil
23 temperament / 13/9 / 8.775586263997216 per mil
23 temperament / 17/3 / 19.23878990559913 per mil
23 temperament / 17/5 / 17.07394928919703 per mil
23 temperament / 17/9 / 4.494361547157544 per mil

23 temperament avg: 16.661474513068786per mil

80 temperament / 3 / 2.5374992788439465 per mil
80 temperament / 4 / 0.0 per mil
80 temperament / 5 / 3.0719051126378294 per mil
80 temperament / 6 / 2.5374992788439465 per mil
80 temperament / 7 / 5.145077942395826 per mil
80 temperament / 8 / 0.0 per mil
80 temperament / 9 / 5.074998557687838 per mil
80 temperament / 10 / 3.0719051126378294 per mil
80 temperament / 11 / 3.06838136270271 per mil
80 temperament / 12 / 2.5374992788439465 per mil
80 temperament / 13 / 0.43971814109222684 per mil
80 temperament / 14 / 5.145077942395826 per mil
80 temperament / 15 / 5.609404391481276 per mil
80 temperament / 16 / 0.0 per mil
80 temperament / 17 / 0.03715874966089827 per mil
80 temperament / 18 / 5.074998557687838 per mil
80 temperament / 5/3 / 0.5344058337938273 per mil
80 temperament / 7/3 / 2.607578663551907 per mil
80 temperament / 11/3 / 0.5308820838589856 per mil
80 temperament / 11/5 / 0.0035237499351192803 per mil
80 temperament / 13/3 / 2.97721741993566 per mil
80 temperament / 13/5 / 3.5116232537297787 per mil
80 temperament / 13/9 / 5.514716698779787 per mil
80 temperament / 17/3 / 2.5003405291834646 per mil
80 temperament / 17/5 / 3.034746362976959 per mil
80 temperament / 17/9 / 5.037839808027078 per mil

80 temperament avg: 4.350249881917781per mil

263 temperament / 3 / 0.5888300773230215 per mil
263 temperament / 4 / 0.0 per mil
263 temperament / 5 / 1.2658214624476916 per mil
263 temperament / 6 / 0.5888300773230215 per mil
263 temperament / 7 / 1.271271867490098 per mil
263 temperament / 8 / 0.0 per mil
263 temperament / 9 / 1.1776601546460153 per mil
263 temperament / 10 / 1.2658214624476916 per mil
263 temperament / 11 / 0.6444269900791055 per mil
263 temperament / 12 / 0.5888300773230215 per mil
263 temperament / 13 / 0.8199462779743261 per mil
263 temperament / 14 / 1.271271867490098 per mil
263 temperament / 15 / 1.854651539770269 per mil
263 temperament / 16 / 0.0 per mil
263 temperament / 17 / 0.010369767449364131 per mil
263 temperament / 18 / 1.1776601546460153 per mil
263 temperament / 5/3 / 0.676991385124559 per mil
263 temperament / 7/3 / 1.8601019448131195 per mil
263 temperament / 11/3 / 0.05559691275636158 per mil
263 temperament / 11/5 / 0.621394472368586 per mil
263 temperament / 13/3 / 1.4087763552968757 per mil
263 temperament / 13/5 / 1.7165136283994742 per mil
263 temperament / 13/9 / 1.8046749362011782 per mil
263 temperament / 17/3 / 0.5991998447728575 per mil
263 temperament / 17/5 / 1.2761912298970834 per mil
263 temperament / 17/9 / 1.188029922095546 per mil

263 temperament avg: 1.4833039005084612per mil

343 temperament / 3 / 1.043330182634028 per mil
343 temperament / 4 / 0.0 per mil
343 temperament / 5 / 1.228386432551687 per mil
343 temperament / 6 / 1.043330182634028 per mil
343 temperament / 7 / 0.22525286950947354 per mil
343 temperament / 8 / 0.0 per mil
343 temperament / 9 / 0.8287915297757187 per mil
343 temperament / 10 / 1.228386432551687 per mil
343 temperament / 11 / 1.2097807796123128 per mil
343 temperament / 12 / 1.043330182634028 per mil
343 temperament / 13 / 0.7312633305965877 per mil
343 temperament / 14 / 0.22525286950947354 per mil
343 temperament / 15 / 0.1850562499181585 per mil
343 temperament / 16 / 0.0 per mil
343 temperament / 17 / 0.0007156009728531698 per mil
343 temperament / 18 / 0.8287915297757187 per mil
343 temperament / 5/3 / 0.6437352798579488 per mil
343 temperament / 7/3 / 0.8180773131244712 per mil
343 temperament / 11/3 / 0.16645059697850684 per mil
343 temperament / 11/5 / 0.47728468287974724 per mil
343 temperament / 13/3 / 1.140858381813603 per mil
343 temperament / 13/5 / 0.4971231019553768 per mil
343 temperament / 13/9 / 0.09752819917940858 per mil
343 temperament / 17/3 / 1.0426145816615495 per mil
343 temperament / 17/5 / 1.229102033524554 per mil
343 temperament / 17/9 / 0.8295071307484747 per mil

343 temperament avg: 1.047746842149962per mil

4036 temperament / 3 / 0.02263307468142184 per mil
4036 temperament / 4 / 0.0 per mil
4036 temperament / 5 / 0.0747747684325395 per mil
4036 temperament / 6 / 0.02263307468142184 per mil
4036 temperament / 7 / 0.12003603183607936 per mil
4036 temperament / 8 / 0.0 per mil
4036 temperament / 9 / 0.045266149362788166 per mil
4036 temperament / 10 / 0.0747747684325395 per mil
4036 temperament / 11 / 0.06591001489891779 per mil
4036 temperament / 12 / 0.02263307468142184 per mil
4036 temperament / 13 / 0.006267983783891928 per mil
4036 temperament / 14 / 0.12003603183607936 per mil
4036 temperament / 15 / 0.052141693751561746 per mil
4036 temperament / 16 / 0.0 per mil
4036 temperament / 17 / 6.760745435707705e-06 per mil
4036 temperament / 18 / 0.045266149362788166 per mil
4036 temperament / 5/3 / 0.09740784311407236 per mil
4036 temperament / 7/3 / 0.10510096285815118 per mil
4036 temperament / 11/3 / 0.08854308958006207 per mil
4036 temperament / 11/5 / 0.008864753533649461 per mil
4036 temperament / 13/3 / 0.016365090897016432 per mil
4036 temperament / 13/5 / 0.08104275221670898 per mil
4036 temperament / 13/9 / 0.03899816557861868 per mil
4036 temperament / 17/3 / 0.02263983542727388 per mil
4036 temperament / 17/5 / 0.07476800768713154 per mil
4036 temperament / 17/9 / 0.04527291010836265 per mil

4036 temperament avg: 0.07821143671799588per mil

32631 temperament / 3 / 0.002716403663893807 per mil
32631 temperament / 4 / 0.0 per mil
32631 temperament / 5 / 0.0050361843181301325 per mil
32631 temperament / 6 / 0.002716403663893807 per mil
32631 temperament / 7 / 0.006176284463199622 per mil
32631 temperament / 8 / 0.0 per mil
32631 temperament / 9 / 0.005432807327759859 per mil
32631 temperament / 10 / 0.0050361843181301325 per mil
32631 temperament / 11 / 0.008790789321533321 per mil
32631 temperament / 12 / 0.002716403663893807 per mil
32631 temperament / 13 / 0.0014845595286416824 per mil
32631 temperament / 14 / 0.006176284463199622 per mil
32631 temperament / 15 / 0.00775258798157985 per mil
32631 temperament / 16 / 0.0 per mil
32631 temperament / 17 / 8.323430139567378e-07 per mil
32631 temperament / 18 / 0.005432807327759859 per mil
32631 temperament / 5/3 / 0.002319780654125303 per mil
32631 temperament / 7/3 / 0.0034598807993058145 per mil
32631 temperament / 11/3 / 0.00607438565791707 per mil
32631 temperament / 11/5 / 0.003754605003430944 per mil
32631 temperament / 13/3 / 0.0042009631920775226 per mil
32631 temperament / 13/5 / 0.00652074384654977 per mil
32631 temperament / 13/9 / 0.006917366856207252 per mil
32631 temperament / 17/3 / 0.0027155713212545507 per mil
32631 temperament / 17/5 / 0.005035351975157809 per mil
32631 temperament / 17/9 / 0.005431974984815291 per mil

32631 temperament avg: 0.006618697292216924per mil

36667 temperament / 3 / 0.004908666031311348 per mil
36667 temperament / 4 / 0.0 per mil
36667 temperament / 5 / 0.003748745054377167 per mil
36667 temperament / 6 / 0.004908666031311348 per mil
36667 temperament / 7 / 0.007716123112677664 per mil
36667 temperament / 8 / 0.0 per mil
36667 temperament / 9 / 0.009817332062622697 per mil
36667 temperament / 10 / 0.003748745054377167 per mil
36667 temperament / 11 / 0.0005683428210279118 per mil
36667 temperament / 12 / 0.004908666031311348 per mil
36667 temperament / 13 / 0.0006312237005312582 per mil
36667 temperament / 14 / 0.007716123112677664 per mil
36667 temperament / 15 / 0.001159920976490092 per mil
36667 temperament / 16 / 0.0 per mil
36667 temperament / 17 / 3.44134443164279e-09 per mil
36667 temperament / 18 / 0.009817332062622697 per mil
36667 temperament / 5/3 / 0.008657411085799538 per mil
36667 temperament / 7/3 / 0.012624789143989013 per mil
36667 temperament / 11/3 / 0.004340323210061392 per mil
36667 temperament / 11/5 / 0.0043170878754328346 per mil
36667 temperament / 13/3 / 0.005539889731398517 per mil
36667 temperament / 13/5 / 0.0031175213540679536 per mil
36667 temperament / 13/9 / 0.01044855576293191 per mil
36667 temperament / 17/3 / 0.004908669473113747 per mil
36667 temperament / 17/5 / 0.0037487416130188578 per mil
36667 temperament / 17/9 / 0.009817335504092028 per mil

36667 temperament avg: 0.007948138390411787per mil


"""

# --- 파싱 및 데이터 정리 ---

# 각 행에서 temperament, ratio, value 분리
pattern = re.compile(r'(\d+)\s+temperament\s+/\s+([\d/]+)\s+/\s+([0-9.eE+-]+) per mil')

data_dict = {}
ratios_set = set()
temperaments_set = set()

for line in data.strip().splitlines():
    line = line.strip()
    if not line:
        continue
    match = pattern.match(line)
    if match:
        temperament = match.group(1)
        ratio = match.group(2)
        value = float(match.group(3))

        temperaments_set.add(temperament)
        ratios_set.add(ratio)

        if temperament not in data_dict:
            data_dict[temperament] = {}
        data_dict[temperament][ratio] = value
    else:
        print("파싱 실패:", line)

# 정렬
temperaments = sorted(temperaments_set, key=int)
# ratio는 단순 숫자와 분수 섞여있으므로 정렬 커스텀
def ratio_key(r):
    if '/' in r:
        nums = list(map(int, r.split('/')))
        return (nums[0]/nums[1], r)
    else:
        return (int(r), r)
ratios = sorted(ratios_set, key=ratio_key)

# --- CSV 작성 ---
with open('temperament_ratio.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['Temperament\\Ratio'] + ratios
    writer.writerow(header)

    for t in temperaments:
        row = [t]
        for r in ratios:
            val = data_dict.get(t, {}).get(r, '')
            row.append(val)
        writer.writerow(row)

print("CSV 파일 'temperament_ratio.csv' 생성 완료")