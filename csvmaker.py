import csv
import re

data = """
1 temperament / 3 / 415.03749927884394 per mil
1 temperament / 4 / 0.0 per mil
1 temperament / 5 / 321.9280948873622 per mil
1 temperament / 6 / 415.03749927884394 per mil
1 temperament / 7 / 192.64507794239583 per mil
1 temperament / 8 / 0.0 per mil
1 temperament / 9 / 169.92500144231215 per mil
1 temperament / 10 / 321.9280948873622 per mil
1 temperament / 11 / 459.43161863729733 per mil
1 temperament / 12 / 415.03749927884394 per mil
1 temperament / 13 / 299.56028185890784 per mil
1 temperament / 14 / 192.64507794239583 per mil
1 temperament / 15 / 93.10940439148129 per mil
1 temperament / 16 / 0.0 per mil
1 temperament / 17 / 87.4628412503391 per mil
1 temperament / 18 / 169.92500144231215 per mil
1 temperament / 5/3 / 263.03440583379376 per mil
1 temperament / 7/3 / 222.3924213364481 per mil
1 temperament / 11/3 / 125.53088208385898 per mil
1 temperament / 11/5 / 137.50352374993514 per mil
1 temperament / 13/3 / 115.47721741993567 per mil
1 temperament / 13/5 / 378.5116232537298 per mil
1 temperament / 13/9 / 469.4852833012202 per mil
1 temperament / 17/3 / 497.49965947081654 per mil
1 temperament / 17/5 / 234.4652536370231 per mil
1 temperament / 17/9 / 82.46216019197294 per mil


2 temperament / 3 / 84.96250072115608 per mil
2 temperament / 4 / 0.0 per mil
2 temperament / 5 / 178.0719051126378 per mil
2 temperament / 6 / 84.96250072115608 per mil
2 temperament / 7 / 192.64507794239583 per mil
2 temperament / 8 / 0.0 per mil
2 temperament / 9 / 169.92500144231215 per mil
2 temperament / 10 / 178.0719051126378 per mil
2 temperament / 11 / 40.56838136270269 per mil
2 temperament / 12 / 84.96250072115608 per mil
2 temperament / 13 / 200.4397181410922 per mil
2 temperament / 14 / 192.64507794239583 per mil
2 temperament / 15 / 93.10940439148129 per mil
2 temperament / 16 / 0.0 per mil
2 temperament / 17 / 87.4628412503391 per mil
2 temperament / 18 / 169.92500144231215 per mil
2 temperament / 5/3 / 236.96559416620622 per mil
2 temperament / 7/3 / 222.3924213364481 per mil
2 temperament / 11/3 / 125.53088208385898 per mil
2 temperament / 11/5 / 137.50352374993514 per mil
2 temperament / 13/3 / 115.47721741993567 per mil
2 temperament / 13/5 / 121.48837674627022 per mil
2 temperament / 13/9 / 30.514716698779807 per mil
2 temperament / 17/3 / 2.5003405291834646 per mil
2 temperament / 17/5 / 234.4652536370231 per mil
2 temperament / 17/9 / 82.46216019197294 per mil


3 temperament / 3 / 81.70416594551055 per mil
3 temperament / 4 / 0.0 per mil
3 temperament / 5 / 11.405238445971133 per mil
3 temperament / 6 / 81.70416594551055 per mil
3 temperament / 7 / 140.68825539093754 per mil
3 temperament / 8 / 0.0 per mil
3 temperament / 9 / 163.40833189102116 per mil
3 temperament / 10 / 11.405238445971133 per mil
3 temperament / 11 / 126.09828530396399 per mil
3 temperament / 12 / 81.70416594551055 per mil
3 temperament / 13 / 33.77305147442555 per mil
3 temperament / 14 / 140.68825539093754 per mil
3 temperament / 15 / 93.10940439148129 per mil
3 temperament / 16 / 0.0 per mil
3 temperament / 17 / 87.4628412503391 per mil
3 temperament / 18 / 163.40833189102116 per mil
3 temperament / 5/3 / 70.29892749953959 per mil
3 temperament / 7/3 / 110.94091199688522 per mil
3 temperament / 11/3 / 125.53088208385898 per mil
3 temperament / 11/5 / 137.50352374993514 per mil
3 temperament / 13/3 / 115.47721741993567 per mil
3 temperament / 13/5 / 45.178289920396466 per mil
3 temperament / 13/9 / 136.15194996788682 per mil
3 temperament / 17/3 / 164.16632613748317 per mil
3 temperament / 17/5 / 98.86807969631029 per mil
3 temperament / 17/9 / 82.46216019197294 per mil


4 temperament / 3 / 84.96250072115608 per mil
4 temperament / 4 / 0.0 per mil
4 temperament / 5 / 71.92809488736218 per mil
4 temperament / 6 / 84.96250072115608 per mil
4 temperament / 7 / 57.35492205760417 per mil
4 temperament / 8 / 0.0 per mil
4 temperament / 9 / 80.07499855768785 per mil
4 temperament / 10 / 71.92809488736218 per mil
4 temperament / 11 / 40.56838136270269 per mil
4 temperament / 12 / 84.96250072115608 per mil
4 temperament / 13 / 49.560281858907814 per mil
4 temperament / 14 / 57.35492205760417 per mil
4 temperament / 15 / 93.10940439148129 per mil
4 temperament / 16 / 0.0 per mil
4 temperament / 17 / 87.4628412503391 per mil
4 temperament / 18 / 80.07499855768785 per mil
4 temperament / 5/3 / 13.034405833793784 per mil
4 temperament / 7/3 / 27.6075786635519 per mil
4 temperament / 11/3 / 124.46911791614102 per mil
4 temperament / 11/5 / 112.49647625006487 per mil
4 temperament / 13/3 / 115.47721741993567 per mil
4 temperament / 13/5 / 121.48837674627022 per mil
4 temperament / 13/9 / 30.514716698779807 per mil
4 temperament / 17/3 / 2.5003405291834646 per mil
4 temperament / 17/5 / 15.534746362976914 per mil
4 temperament / 17/9 / 82.46216019197294 per mil


5 temperament / 3 / 15.037499278843903 per mil
5 temperament / 4 / 0.0 per mil
5 temperament / 5 / 78.07190511263784 per mil
5 temperament / 6 / 15.037499278843903 per mil
5 temperament / 7 / 7.35492205760413 per mil
5 temperament / 8 / 0.0 per mil
5 temperament / 9 / 30.07499855768786 per mil
5 temperament / 10 / 78.07190511263784 per mil
5 temperament / 11 / 59.43161863729729 per mil
5 temperament / 12 / 15.037499278843903 per mil
5 temperament / 13 / 99.56028185890786 per mil
5 temperament / 14 / 7.35492205760413 per mil
5 temperament / 15 / 93.10940439148129 per mil
5 temperament / 16 / 0.0 per mil
5 temperament / 17 / 87.4628412503391 per mil
5 temperament / 18 / 30.07499855768786 per mil
5 temperament / 5/3 / 63.034405833793826 per mil
5 temperament / 7/3 / 22.392421336448088 per mil
5 temperament / 11/3 / 74.46911791614097 per mil
5 temperament / 11/5 / 62.49647625006488 per mil
5 temperament / 13/3 / 84.52278258006434 per mil
5 temperament / 13/5 / 21.488376746270244 per mil
5 temperament / 13/9 / 69.48528330122016 per mil
5 temperament / 17/3 / 97.49965947081651 per mil
5 temperament / 17/5 / 34.46525363702313 per mil
5 temperament / 17/9 / 82.46216019197294 per mil


6 temperament / 3 / 81.70416594551055 per mil
6 temperament / 4 / 0.0 per mil
6 temperament / 5 / 11.405238445971133 per mil
6 temperament / 6 / 81.70416594551055 per mil
6 temperament / 7 / 25.978411275729197 per mil
6 temperament / 8 / 0.0 per mil
6 temperament / 9 / 3.258334775645494 per mil
6 temperament / 10 / 11.405238445971133 per mil
6 temperament / 11 / 40.56838136270269 per mil
6 temperament / 12 / 81.70416594551055 per mil
6 temperament / 13 / 33.77305147442555 per mil
6 temperament / 14 / 25.978411275729197 per mil
6 temperament / 15 / 73.55726227518534 per mil
6 temperament / 16 / 0.0 per mil
6 temperament / 17 / 79.20382541632756 per mil
6 temperament / 18 / 3.258334775645494 per mil
6 temperament / 5/3 / 70.29892749953959 per mil
6 temperament / 7/3 / 55.72575466978144 per mil
6 temperament / 11/3 / 41.135784582807645 per mil
6 temperament / 11/5 / 29.163142916731527 per mil
6 temperament / 13/3 / 51.189449246730995 per mil
6 temperament / 13/5 / 45.178289920396466 per mil
6 temperament / 13/9 / 30.514716698779807 per mil
6 temperament / 17/3 / 2.5003405291834646 per mil
6 temperament / 17/5 / 67.79858697035645 per mil
6 temperament / 17/9 / 82.46216019197294 per mil


7 temperament / 3 / 13.533929292584679 per mil
7 temperament / 4 / 0.0 per mil
7 temperament / 5 / 36.213809173076484 per mil
7 temperament / 6 / 13.533929292584679 per mil
7 temperament / 7 / 49.78793508525292 per mil
7 temperament / 8 / 0.0 per mil
7 temperament / 9 / 27.0678585851693 per mil
7 temperament / 10 / 36.213809173076484 per mil
7 temperament / 11 / 30.860190065868764 per mil
7 temperament / 12 / 13.533929292584679 per mil
7 temperament / 13 / 13.84599614462212 per mil
7 temperament / 14 / 49.78793508525292 per mil
7 temperament / 15 / 49.747738465661605 per mil
7 temperament / 16 / 0.0 per mil
7 temperament / 17 / 55.39430160680375 per mil
7 temperament / 18 / 27.0678585851693 per mil
7 temperament / 5/3 / 22.679879880491917 per mil
7 temperament / 7/3 / 63.3218643778376 per mil
7 temperament / 11/3 / 17.32626077328392 per mil
7 temperament / 11/5 / 5.353619107207718 per mil
7 temperament / 13/3 / 27.379925437207188 per mil
7 temperament / 13/5 / 50.05980531769877 per mil
7 temperament / 13/9 / 40.91385472979159 per mil
7 temperament / 17/3 / 68.92823089938793 per mil
7 temperament / 17/5 / 51.24903207726261 per mil
7 temperament / 17/9 / 60.39498266516996 per mil


8 temperament / 3 / 40.037499278843924 per mil
8 temperament / 4 / 0.0 per mil
8 temperament / 5 / 53.07190511263782 per mil
8 temperament / 6 / 40.037499278843924 per mil
8 temperament / 7 / 57.35492205760417 per mil
8 temperament / 8 / 0.0 per mil
8 temperament / 9 / 44.92500144231215 per mil
8 temperament / 10 / 53.07190511263782 per mil
8 temperament / 11 / 40.56838136270269 per mil
8 temperament / 12 / 40.037499278843924 per mil
8 temperament / 13 / 49.560281858907814 per mil
8 temperament / 14 / 57.35492205760417 per mil
8 temperament / 15 / 31.8905956085187 per mil
8 temperament / 16 / 0.0 per mil
8 temperament / 17 / 37.537158749660904 per mil
8 temperament / 18 / 44.92500144231215 per mil
8 temperament / 5/3 / 13.034405833793784 per mil
8 temperament / 7/3 / 27.6075786635519 per mil
8 temperament / 11/3 / 0.5308820838589856 per mil
8 temperament / 11/5 / 12.50352374993513 per mil
8 temperament / 13/3 / 9.522782580064337 per mil
8 temperament / 13/5 / 3.5116232537297787 per mil
8 temperament / 13/9 / 30.514716698779807 per mil
8 temperament / 17/3 / 2.5003405291834646 per mil
8 temperament / 17/5 / 15.534746362976914 per mil
8 temperament / 17/9 / 42.53783980802706 per mil


9 temperament / 3 / 29.406945165600497 per mil
9 temperament / 4 / 0.0 per mil
9 temperament / 5 / 11.405238445971133 per mil
9 temperament / 6 / 29.406945165600497 per mil
9 temperament / 7 / 29.577144279826385 per mil
9 temperament / 8 / 0.0 per mil
9 temperament / 9 / 52.297220779910056 per mil
9 temperament / 10 / 11.405238445971133 per mil
9 temperament / 11 / 14.987174192852892 per mil
9 temperament / 12 / 29.406945165600497 per mil
9 temperament / 13 / 33.77305147442555 per mil
9 temperament / 14 / 29.577144279826385 per mil
9 temperament / 15 / 18.001706719629862 per mil
9 temperament / 16 / 0.0 per mil
9 temperament / 17 / 23.648269860772007 per mil
9 temperament / 18 / 52.297220779910056 per mil
9 temperament / 5/3 / 40.81218361157157 per mil
9 temperament / 7/3 / 0.17019911422588851 per mil
9 temperament / 11/3 / 14.419770972747825 per mil
9 temperament / 11/5 / 26.392412638824027 per mil
9 temperament / 13/3 / 4.366106308824557 per mil
9 temperament / 13/5 / 45.178289920396466 per mil
9 temperament / 13/9 / 25.04083885677577 per mil
9 temperament / 17/3 / 53.05521502637212 per mil
9 temperament / 17/5 / 12.243031414800875 per mil
9 temperament / 17/9 / 28.648950919138215 per mil


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


14 temperament / 3 / 13.533929292584679 per mil
14 temperament / 4 / 0.0 per mil
14 temperament / 5 / 35.21476225549497 per mil
14 temperament / 6 / 13.533929292584679 per mil
14 temperament / 7 / 21.640636343318477 per mil
14 temperament / 8 / 0.0 per mil
14 temperament / 9 / 27.0678585851693 per mil
14 temperament / 10 / 35.21476225549497 per mil
14 temperament / 11 / 30.860190065868764 per mil
14 temperament / 12 / 13.533929292584679 per mil
14 temperament / 13 / 13.84599614462212 per mil
14 temperament / 14 / 21.640636343318477 per mil
14 temperament / 15 / 21.680832962909903 per mil
14 temperament / 16 / 0.0 per mil
14 temperament / 17 / 16.034269821767673 per mil
14 temperament / 18 / 27.0678585851693 per mil
14 temperament / 5/3 / 22.679879880491917 per mil
14 temperament / 7/3 / 8.106707050733824 per mil
14 temperament / 11/3 / 17.32626077328392 per mil
14 temperament / 11/5 / 5.353619107207718 per mil
14 temperament / 13/3 / 27.379925437207188 per mil
14 temperament / 13/5 / 21.368766110872627 per mil
14 temperament / 13/9 / 30.514716698779807 per mil
14 temperament / 17/3 / 2.5003405291834646 per mil
14 temperament / 17/5 / 20.179539351308783 per mil
14 temperament / 17/9 / 11.033588763401546 per mil


15 temperament / 3 / 15.037499278843903 per mil
15 temperament / 4 / 0.0 per mil
15 temperament / 5 / 11.405238445971133 per mil
15 temperament / 6 / 15.037499278843903 per mil
15 temperament / 7 / 7.35492205760413 per mil
15 temperament / 8 / 0.0 per mil
15 temperament / 9 / 30.07499855768786 per mil
15 temperament / 10 / 11.405238445971133 per mil
15 temperament / 11 / 7.235048029369362 per mil
15 temperament / 12 / 15.037499278843903 per mil
15 temperament / 13 / 32.8936151922411 per mil
15 temperament / 14 / 7.35492205760413 per mil
15 temperament / 15 / 26.44273772481465 per mil
15 temperament / 16 / 0.0 per mil
15 temperament / 17 / 20.796174583672432 per mil
15 temperament / 18 / 30.07499855768786 per mil
15 temperament / 5/3 / 3.6322608328729356 per mil
15 temperament / 7/3 / 22.392421336448088 per mil
15 temperament / 11/3 / 7.802451249474318 per mil
15 temperament / 11/5 / 4.170190416601799 per mil
15 temperament / 13/3 / 17.85611591339767 per mil
15 temperament / 13/5 / 21.488376746270244 per mil
15 temperament / 13/9 / 2.818616634553517 per mil
15 temperament / 17/3 / 30.83299280414986 per mil
15 temperament / 17/5 / 32.20141302964363 per mil
15 temperament / 17/9 / 15.795493525306291 per mil


16 temperament / 3 / 22.462500721156076 per mil
16 temperament / 4 / 0.0 per mil
16 temperament / 5 / 9.428094887362182 per mil
16 temperament / 6 / 22.462500721156076 per mil
16 temperament / 7 / 5.145077942395826 per mil
16 temperament / 8 / 0.0 per mil
16 temperament / 9 / 17.57499855768785 per mil
16 temperament / 10 / 9.428094887362182 per mil
16 temperament / 11 / 21.931618637297312 per mil
16 temperament / 12 / 22.462500721156076 per mil
16 temperament / 13 / 12.939718141092182 per mil
16 temperament / 14 / 5.145077942395826 per mil
16 temperament / 15 / 30.6094043914813 per mil
16 temperament / 16 / 0.0 per mil
16 temperament / 17 / 24.962841250339096 per mil
16 temperament / 18 / 17.57499855768785 per mil
16 temperament / 5/3 / 13.034405833793784 per mil
16 temperament / 7/3 / 27.6075786635519 per mil
16 temperament / 11/3 / 0.5308820838589856 per mil
16 temperament / 11/5 / 12.50352374993513 per mil
16 temperament / 13/3 / 9.522782580064337 per mil
16 temperament / 13/5 / 3.5116232537297787 per mil
16 temperament / 13/9 / 30.514716698779807 per mil
16 temperament / 17/3 / 2.5003405291834646 per mil
16 temperament / 17/5 / 15.534746362976914 per mil
16 temperament / 17/9 / 19.962160191972945 per mil


17 temperament / 3 / 3.2727933964910028 per mil
17 temperament / 4 / 0.0 per mil
17 temperament / 5 / 27.810447828538642 per mil
17 temperament / 6 / 3.2727933964910028 per mil
17 temperament / 7 / 16.17448970710167 per mil
17 temperament / 8 / 0.0 per mil
17 temperament / 9 / 6.545586792981978 per mil
17 temperament / 10 / 27.810447828538642 per mil
17 temperament / 11 / 11.15661665682033 per mil
17 temperament / 12 / 3.2727933964910028 per mil
17 temperament / 13 / 5.442634800084334 per mil
17 temperament / 14 / 16.17448970710167 per mil
17 temperament / 15 / 24.53765443204814 per mil
17 temperament / 16 / 0.0 per mil
17 temperament / 17 / 28.63931183857439 per mil
17 temperament / 18 / 6.545586792981978 per mil
17 temperament / 5/3 / 27.740288186734908 per mil
17 temperament / 7/3 / 12.901696310610722 per mil
17 temperament / 11/3 / 7.883823260329548 per mil
17 temperament / 11/5 / 19.85646492640572 per mil
17 temperament / 13/3 / 2.1698414035937477 per mil
17 temperament / 13/5 / 25.57044678314152 per mil
17 temperament / 13/9 / 1.1029519928974496 per mil
17 temperament / 17/3 / 26.911424176698894 per mil
17 temperament / 17/5 / 0.8288640100357902 per mil
17 temperament / 17/9 / 23.638630780208224 per mil


18 temperament / 3 / 26.148610389955085 per mil
18 temperament / 4 / 0.0 per mil
18 temperament / 5 / 11.405238445971133 per mil
18 temperament / 6 / 26.148610389955085 per mil
18 temperament / 7 / 25.978411275729197 per mil
18 temperament / 8 / 0.0 per mil
18 temperament / 9 / 3.258334775645494 per mil
18 temperament / 10 / 11.405238445971133 per mil
18 temperament / 11 / 14.987174192852892 per mil
18 temperament / 12 / 26.148610389955085 per mil
18 temperament / 13 / 21.78250408113003 per mil
18 temperament / 14 / 25.978411275729197 per mil
18 temperament / 15 / 18.001706719629862 per mil
18 temperament / 16 / 0.0 per mil
18 temperament / 17 / 23.648269860772007 per mil
18 temperament / 18 / 3.258334775645494 per mil
18 temperament / 5/3 / 14.743371943984007 per mil
18 temperament / 7/3 / 0.17019911422588851 per mil
18 temperament / 11/3 / 14.419770972747825 per mil
18 temperament / 11/5 / 26.392412638824027 per mil
18 temperament / 13/3 / 4.366106308824557 per mil
18 temperament / 13/5 / 10.377265635159116 per mil
18 temperament / 13/9 / 25.04083885677577 per mil
18 temperament / 17/3 / 2.5003405291834646 per mil
18 temperament / 17/5 / 12.243031414800875 per mil
18 temperament / 17/9 / 26.906604636417363 per mil


19 temperament / 3 / 6.015132300103421 per mil
19 temperament / 4 / 0.0 per mil
19 temperament / 5 / 6.138621203151673 per mil
19 temperament / 6 / 6.015132300103421 per mil
19 temperament / 7 / 17.88123784707785 per mil
19 temperament / 8 / 0.0 per mil
19 temperament / 9 / 12.030264600206896 per mil
19 temperament / 10 / 6.138621203151673 per mil
19 temperament / 11 / 14.25259188901845 per mil
19 temperament / 12 / 6.015132300103421 per mil
19 temperament / 13 / 16.229191825302692 per mil
19 temperament / 14 / 17.88123784707785 per mil
19 temperament / 15 / 12.153753503255537 per mil
19 temperament / 16 / 0.0 per mil
19 temperament / 17 / 17.80031664439774 per mil
19 temperament / 18 / 12.030264600206896 per mil
19 temperament / 5/3 / 0.12348890304836324 per mil
19 temperament / 7/3 / 11.866105546974426 per mil
19 temperament / 11/3 / 20.26772418912215 per mil
19 temperament / 11/5 / 20.391213092170123 per mil
19 temperament / 13/3 / 10.214059525198827 per mil
19 temperament / 13/5 / 10.090570622150851 per mil
19 temperament / 13/9 / 4.198927225095628 per mil
19 temperament / 17/3 / 23.815448944500716 per mil
19 temperament / 17/5 / 23.93893784754941 per mil
19 temperament / 17/9 / 22.800997702763894 per mil


20 temperament / 3 / 15.037499278843903 per mil
20 temperament / 4 / 0.0 per mil
20 temperament / 5 / 21.928094887362192 per mil
20 temperament / 6 / 15.037499278843903 per mil
20 temperament / 7 / 7.35492205760413 per mil
20 temperament / 8 / 0.0 per mil
20 temperament / 9 / 19.92500144231216 per mil
20 temperament / 10 / 21.928094887362192 per mil
20 temperament / 11 / 9.431618637297301 per mil
20 temperament / 12 / 15.037499278843903 per mil
20 temperament / 13 / 0.43971814109222684 per mil
20 temperament / 14 / 7.35492205760413 per mil
20 temperament / 15 / 6.890595608518679 per mil
20 temperament / 16 / 0.0 per mil
20 temperament / 17 / 12.53715874966091 per mil
20 temperament / 18 / 19.92500144231216 per mil
20 temperament / 5/3 / 13.034405833793784 per mil
20 temperament / 7/3 / 22.392421336448088 per mil
20 temperament / 11/3 / 24.469117916141037 per mil
20 temperament / 11/5 / 12.496476250064864 per mil
20 temperament / 13/3 / 15.477217419935657 per mil
20 temperament / 13/5 / 21.488376746270244 per mil
20 temperament / 13/9 / 19.485283301220235 per mil
20 temperament / 17/3 / 2.5003405291834646 per mil
20 temperament / 17/5 / 15.534746362976914 per mil
20 temperament / 17/9 / 17.537839808027034 per mil


21 temperament / 3 / 13.533929292584679 per mil
21 temperament / 4 / 0.0 per mil
21 temperament / 5 / 11.405238445971133 per mil
21 temperament / 6 / 13.533929292584679 per mil
21 temperament / 7 / 2.1688874662053603 per mil
21 temperament / 8 / 0.0 per mil
21 temperament / 9 / 20.551189033878316 per mil
21 temperament / 10 / 11.405238445971133 per mil
21 temperament / 11 / 16.758857553178853 per mil
21 temperament / 12 / 13.533929292584679 per mil
21 temperament / 13 / 13.84599614462212 per mil
21 temperament / 14 / 2.1688874662053603 per mil
21 temperament / 15 / 2.1286908466139343 per mil
21 temperament / 16 / 0.0 per mil
21 temperament / 17 / 7.775253987756137 per mil
21 temperament / 18 / 20.551189033878316 per mil
21 temperament / 5/3 / 22.679879880491917 per mil
21 temperament / 7/3 / 15.702816758789984 per mil
21 temperament / 11/3 / 17.32626077328392 per mil
21 temperament / 11/5 / 5.353619107207718 per mil
21 temperament / 13/3 / 20.23912218184043 per mil
21 temperament / 13/5 / 2.4407576986511526 per mil
21 temperament / 13/9 / 6.705192889255973 per mil
21 temperament / 17/3 / 21.30918328034037 per mil
21 temperament / 17/5 / 3.629984458215052 per mil
21 temperament / 17/9 / 12.775935046122289 per mil


22 temperament / 3 / 5.946590187934864 per mil
22 temperament / 4 / 0.0 per mil
22 temperament / 5 / 3.746276705544005 per mil
22 temperament / 6 / 5.946590187934864 per mil
22 temperament / 7 / 10.82689612421406 per mil
22 temperament / 8 / 0.0 per mil
22 temperament / 9 / 11.893180375869672 per mil
22 temperament / 10 / 3.746276705544005 per mil
22 temperament / 11 / 4.886164091842781 per mil
22 temperament / 12 / 5.946590187934864 per mil
22 temperament / 13 / 18.621536322910416 per mil
22 temperament / 14 / 10.82689612421406 per mil
22 temperament / 15 / 2.200313482390359 per mil
22 temperament / 16 / 0.0 per mil
22 temperament / 17 / 3.4462496587518157 per mil
22 temperament / 18 / 11.893180375869672 per mil
22 temperament / 5/3 / 9.692866893478925 per mil
22 temperament / 7/3 / 4.880305936279167 per mil
22 temperament / 11/3 / 10.832754279777369 per mil
22 temperament / 11/5 / 1.1398873862987768 per mil
22 temperament / 13/3 / 20.88641894370069 per mil
22 temperament / 13/5 / 14.875259617366133 per mil
22 temperament / 13/9 / 14.939828755765605 per mil
22 temperament / 17/3 / 2.5003405291834646 per mil
22 temperament / 17/5 / 7.192526364295793 per mil
22 temperament / 17/9 / 8.446930717117995 per mil


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


25 temperament / 3 / 15.037499278843903 per mil
25 temperament / 4 / 0.0 per mil
25 temperament / 5 / 1.928094887362175 per mil
25 temperament / 6 / 15.037499278843903 per mil
25 temperament / 7 / 7.35492205760413 per mil
25 temperament / 8 / 0.0 per mil
25 temperament / 9 / 9.925001442312148 per mil
25 temperament / 10 / 1.928094887362175 per mil
25 temperament / 11 / 19.43161863729731 per mil
25 temperament / 12 / 15.037499278843903 per mil
25 temperament / 13 / 19.560281858907793 per mil
25 temperament / 14 / 7.35492205760413 per mil
25 temperament / 15 / 13.109404391481338 per mil
25 temperament / 16 / 0.0 per mil
25 temperament / 17 / 7.462841250339094 per mil
25 temperament / 18 / 9.925001442312148 per mil
25 temperament / 5/3 / 16.965594166206245 per mil
25 temperament / 7/3 / 17.60757866355189 per mil
25 temperament / 11/3 / 5.53088208385899 per mil
25 temperament / 11/5 / 17.503523749935134 per mil
25 temperament / 13/3 / 4.522782580064333 per mil
25 temperament / 13/5 / 18.51162325372979 per mil
25 temperament / 13/9 / 10.514716698779791 per mil
25 temperament / 17/3 / 17.499659470816553 per mil
25 temperament / 17/5 / 5.534746362976906 per mil
25 temperament / 17/9 / 2.462160191972984 per mil


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


27 temperament / 3 / 7.630091871436484 per mil
27 temperament / 4 / 0.0 per mil
27 temperament / 5 / 11.405238445971133 per mil
27 temperament / 6 / 7.630091871436484 per mil
27 temperament / 7 / 7.4598927572105955 per mil
27 temperament / 8 / 0.0 per mil
27 temperament / 9 / 15.260183742873023 per mil
27 temperament / 10 / 11.405238445971133 per mil
27 temperament / 11 / 14.987174192852892 per mil
27 temperament / 12 / 7.630091871436484 per mil
27 temperament / 13 / 3.2639855626115377 per mil
27 temperament / 14 / 7.4598927572105955 per mil
27 temperament / 15 / 18.001706719629862 per mil
27 temperament / 16 / 0.0 per mil
27 temperament / 17 / 13.388767176265027 per mil
27 temperament / 18 / 15.260183742873023 per mil
27 temperament / 5/3 / 3.7751465745344825 per mil
27 temperament / 7/3 / 0.17019911422588851 per mil
27 temperament / 11/3 / 14.419770972747825 per mil
27 temperament / 11/5 / 10.64462439821301 per mil
27 temperament / 13/3 / 4.366106308824557 per mil
27 temperament / 13/5 / 8.141252883359428 per mil
27 temperament / 13/9 / 11.99619818026132 per mil
27 temperament / 17/3 / 16.018177989335026 per mil
27 temperament / 17/5 / 12.243031414800875 per mil
27 temperament / 17/9 / 8.388086117898874 per mil


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


29 temperament / 3 / 1.2443958305680125 per mil
29 temperament / 4 / 0.0 per mil
29 temperament / 5 / 11.583267301155276 per mil
29 temperament / 6 / 1.2443958305680125 per mil
29 temperament / 7 / 14.251473781742074 per mil
29 temperament / 8 / 0.0 per mil
29 temperament / 9 / 2.488791661136136 per mil
29 temperament / 10 / 11.583267301155276 per mil
29 temperament / 11 / 11.155756568331787 per mil
29 temperament / 12 / 1.2443958305680125 per mil
29 temperament / 13 / 10.784545727299033 per mil
29 temperament / 14 / 14.251473781742074 per mil
29 temperament / 15 / 10.338871470587652 per mil
29 temperament / 16 / 0.0 per mil
29 temperament / 17 / 15.985434611729868 per mil
29 temperament / 18 / 2.488791661136136 per mil
29 temperament / 5/3 / 12.827663131723455 per mil
29 temperament / 7/3 / 15.49586961231017 per mil
29 temperament / 11/3 / 12.400152398899689 per mil
29 temperament / 11/5 / 0.4275107328234884 per mil
29 temperament / 13/3 / 12.028941557866698 per mil
29 temperament / 13/5 / 0.7987215738564091 per mil
29 temperament / 13/9 / 13.273337388434946 per mil
29 temperament / 17/3 / 14.741038781161397 per mil
29 temperament / 17/5 / 6.914056707804539 per mil
29 temperament / 17/9 / 13.496642950593607 per mil


30 temperament / 3 / 15.037499278843903 per mil
30 temperament / 4 / 0.0 per mil
30 temperament / 5 / 11.405238445971133 per mil
30 temperament / 6 / 15.037499278843903 per mil
30 temperament / 7 / 7.35492205760413 per mil
30 temperament / 8 / 0.0 per mil
30 temperament / 9 / 3.258334775645494 per mil
30 temperament / 10 / 11.405238445971133 per mil
30 temperament / 11 / 7.235048029369362 per mil
30 temperament / 12 / 15.037499278843903 per mil
30 temperament / 13 / 0.43971814109222684 per mil
30 temperament / 14 / 7.35492205760413 per mil
30 temperament / 15 / 6.890595608518679 per mil
30 temperament / 16 / 0.0 per mil
30 temperament / 17 / 12.53715874966091 per mil
30 temperament / 18 / 3.258334775645494 per mil
30 temperament / 5/3 / 3.6322608328729356 per mil
30 temperament / 7/3 / 10.940911996885239 per mil
30 temperament / 11/3 / 7.802451249474318 per mil
30 temperament / 11/5 / 4.170190416601799 per mil
30 temperament / 13/3 / 15.477217419935657 per mil
30 temperament / 13/5 / 11.844956587063137 per mil
30 temperament / 13/9 / 2.818616634553517 per mil
30 temperament / 17/3 / 2.5003405291834646 per mil
30 temperament / 17/5 / 1.131920303689804 per mil
30 temperament / 17/9 / 15.795493525306291 per mil


31 temperament / 3 / 4.317339430833456 per mil
31 temperament / 4 / 0.0 per mil
31 temperament / 5 / 0.6525502739281319 per mil
31 temperament / 6 / 4.317339430833456 per mil
31 temperament / 7 / 0.9033091543784177 per mil
31 temperament / 8 / 0.0 per mil
31 temperament / 9 / 8.634678861666995 per mil
31 temperament / 10 / 0.6525502739281319 per mil
31 temperament / 11 / 7.818715411490873 per mil
31 temperament / 12 / 4.317339430833456 per mil
31 temperament / 13 / 9.237701213746563 per mil
31 temperament / 14 / 0.9033091543784177 per mil
31 temperament / 15 / 3.6647891569058233 per mil
31 temperament / 16 / 0.0 per mil
31 temperament / 17 / 9.311352298047998 per mil
31 temperament / 18 / 8.634678861666995 per mil
31 temperament / 5/3 / 4.969889704761532 per mil
31 temperament / 7/3 / 3.4140302764551214 per mil
31 temperament / 11/3 / 3.50137598065714 per mil
31 temperament / 11/5 / 8.471265685419006 per mil
31 temperament / 13/3 / 13.555040644580462 per mil
31 temperament / 13/5 / 8.585150939818597 per mil
31 temperament / 13/9 / 14.385684440715307 per mil
31 temperament / 17/3 / 13.628691728881037 per mil
31 temperament / 17/5 / 8.658802024119838 per mil
31 temperament / 17/9 / 14.312033356414178 per mil


32 temperament / 3 / 8.787499278843924 per mil
32 temperament / 4 / 0.0 per mil
32 temperament / 5 / 9.428094887362182 per mil
32 temperament / 6 / 8.787499278843924 per mil
32 temperament / 7 / 5.145077942395826 per mil
32 temperament / 8 / 0.0 per mil
32 temperament / 9 / 13.675001442312151 per mil
32 temperament / 10 / 9.428094887362182 per mil
32 temperament / 11 / 9.318381362702688 per mil
32 temperament / 12 / 8.787499278843924 per mil
32 temperament / 13 / 12.939718141092182 per mil
32 temperament / 14 / 5.145077942395826 per mil
32 temperament / 15 / 0.6405956085187015 per mil
32 temperament / 16 / 0.0 per mil
32 temperament / 17 / 6.287158749660904 per mil
32 temperament / 18 / 13.675001442312151 per mil
32 temperament / 5/3 / 13.034405833793784 per mil
32 temperament / 7/3 / 3.6424213364480984 per mil
32 temperament / 11/3 / 0.5308820838589856 per mil
32 temperament / 11/5 / 12.50352374993513 per mil
32 temperament / 13/3 / 9.522782580064337 per mil
32 temperament / 13/5 / 3.5116232537297787 per mil
32 temperament / 13/9 / 0.7352833012201909 per mil
32 temperament / 17/3 / 2.5003405291834646 per mil
32 temperament / 17/5 / 15.534746362976914 per mil
32 temperament / 17/9 / 11.287839808027055 per mil


33 temperament / 3 / 9.204924963580275 per mil
33 temperament / 4 / 0.0 per mil
33 temperament / 5 / 11.405238445971133 per mil
33 temperament / 6 / 9.204924963580275 per mil
33 temperament / 7 / 10.82689612421406 per mil
33 temperament / 8 / 0.0 per mil
33 temperament / 9 / 11.893180375869672 per mil
33 temperament / 10 / 11.405238445971133 per mil
33 temperament / 11 / 4.886164091842781 per mil
33 temperament / 12 / 9.204924963580275 per mil
33 temperament / 13 / 3.4700211713951656 per mil
33 temperament / 14 / 10.82689612421406 per mil
33 temperament / 15 / 2.200313482390359 per mil
33 temperament / 16 / 0.0 per mil
33 temperament / 17 / 3.4462496587518157 per mil
33 temperament / 18 / 11.893180375869672 per mil
33 temperament / 5/3 / 9.692866893478925 per mil
33 temperament / 7/3 / 10.271209215235972 per mil
33 temperament / 11/3 / 4.31876087173777 per mil
33 temperament / 11/5 / 14.011627765216389 per mil
33 temperament / 13/3 / 5.734903792185553 per mil
33 temperament / 13/5 / 14.875259617366133 per mil
33 temperament / 13/9 / 14.939828755765605 per mil
33 temperament / 17/3 / 12.651174622331673 per mil
33 temperament / 17/5 / 7.958988787219345 per mil
33 temperament / 17/9 / 8.446930717117995 per mil


34 temperament / 3 / 3.2727933964910028 per mil
34 temperament / 4 / 0.0 per mil
34 temperament / 5 / 1.601316877343717 per mil
34 temperament / 6 / 3.2727933964910028 per mil
34 temperament / 7 / 13.237274998780691 per mil
34 temperament / 8 / 0.0 per mil
34 temperament / 9 / 6.545586792981978 per mil
34 temperament / 10 / 1.601316877343717 per mil
34 temperament / 11 / 11.15661665682033 per mil
34 temperament / 12 / 3.2727933964910028 per mil
34 temperament / 13 / 5.442634800084334 per mil
34 temperament / 14 / 13.237274998780691 per mil
34 temperament / 15 / 4.87411027383422 per mil
34 temperament / 16 / 0.0 per mil
34 temperament / 17 / 0.7724528673079684 per mil
34 temperament / 18 / 6.545586792981978 per mil
34 temperament / 5/3 / 1.6714765191473413 per mil
34 temperament / 7/3 / 12.901696310610722 per mil
34 temperament / 11/3 / 7.883823260329548 per mil
34 temperament / 11/5 / 9.55529977947664 per mil
34 temperament / 13/3 / 2.1698414035937477 per mil
34 temperament / 13/5 / 3.8413179227407834 per mil
34 temperament / 13/9 / 1.1029519928974496 per mil
34 temperament / 17/3 / 2.5003405291834646 per mil
34 temperament / 17/5 / 0.8288640100357902 per mil
34 temperament / 17/9 / 5.773133925674134 per mil


35 temperament / 3 / 13.533929292584679 per mil
35 temperament / 4 / 0.0 per mil
35 temperament / 5 / 7.642380601647902 per mil
35 temperament / 6 / 13.533929292584679 per mil
35 temperament / 7 / 7.35492205760413 per mil
35 temperament / 8 / 0.0 per mil
35 temperament / 9 / 1.5035699862592788 per mil
35 temperament / 10 / 7.642380601647902 per mil
35 temperament / 11 / 2.2887614944401835 per mil
35 temperament / 12 / 13.533929292584679 per mil
35 temperament / 13 / 13.84599614462212 per mil
35 temperament / 14 / 7.35492205760413 per mil
35 temperament / 15 / 7.395118677195556 per mil
35 temperament / 16 / 0.0 per mil
35 temperament / 17 / 1.748555536053381 per mil
35 temperament / 18 / 1.5035699862592788 per mil
35 temperament / 5/3 / 5.8915486909366654 per mil
35 temperament / 7/3 / 6.179007234980466 per mil
35 temperament / 11/3 / 11.245167798144662 per mil
35 temperament / 11/5 / 5.353619107207718 per mil
35 temperament / 13/3 / 1.1915031342213807 per mil
35 temperament / 13/5 / 7.083051825158337 per mil
35 temperament / 13/9 / 12.342426158363008 per mil
35 temperament / 17/3 / 11.78537375653077 per mil
35 temperament / 17/5 / 5.893825065594549 per mil
35 temperament / 17/9 / 3.2521255223127987 per mil


36 temperament / 3 / 1.6291673878227053 per mil
36 temperament / 4 / 0.0 per mil
36 temperament / 5 / 11.405238445971133 per mil
36 temperament / 6 / 1.6291673878227053 per mil
36 temperament / 7 / 1.7993665020485938 per mil
36 temperament / 8 / 0.0 per mil
36 temperament / 9 / 3.258334775645494 per mil
36 temperament / 10 / 11.405238445971133 per mil
36 temperament / 11 / 12.790603584924899 per mil
36 temperament / 12 / 1.6291673878227053 per mil
36 temperament / 13 / 5.995273696647763 per mil
36 temperament / 14 / 1.7993665020485938 per mil
36 temperament / 15 / 9.776071058147927 per mil
36 temperament / 16 / 0.0 per mil
36 temperament / 17 / 4.129507917005768 per mil
36 temperament / 18 / 3.258334775645494 per mil
36 temperament / 5/3 / 13.034405833793784 per mil
36 temperament / 7/3 / 0.17019911422588851 per mil
36 temperament / 11/3 / 13.358006805029854 per mil
36 temperament / 11/5 / 1.3853651389537647 per mil
36 temperament / 13/3 / 4.366106308824557 per mil
36 temperament / 13/5 / 10.377265635159116 per mil
36 temperament / 13/9 / 2.736938921002019 per mil
36 temperament / 17/3 / 2.5003405291834646 per mil
36 temperament / 17/5 / 12.243031414800875 per mil
36 temperament / 17/9 / 0.8711731413604262 per mil


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


38 temperament / 3 / 6.015132300103421 per mil
38 temperament / 4 / 0.0 per mil
38 temperament / 5 / 6.138621203151673 per mil
38 temperament / 6 / 6.015132300103421 per mil
38 temperament / 7 / 8.434551626606336 per mil
38 temperament / 8 / 0.0 per mil
38 temperament / 9 / 12.030264600206896 per mil
38 temperament / 10 / 6.138621203151673 per mil
38 temperament / 11 / 12.06319758466573 per mil
38 temperament / 12 / 6.015132300103421 per mil
38 temperament / 13 / 10.08659764838149 per mil
38 temperament / 14 / 8.434551626606336 per mil
38 temperament / 15 / 12.153753503255537 per mil
38 temperament / 16 / 0.0 per mil
38 temperament / 17 / 8.51547282928647 per mil
38 temperament / 18 / 12.030264600206896 per mil
38 temperament / 5/3 / 0.12348890304836324 per mil
38 temperament / 7/3 / 11.866105546974426 per mil
38 temperament / 11/3 / 6.048065284562032 per mil
38 temperament / 11/5 / 5.924576381514085 per mil
38 temperament / 13/3 / 10.214059525198827 per mil
38 temperament / 13/5 / 10.090570622150851 per mil
38 temperament / 13/9 / 4.198927225095628 per mil
38 temperament / 17/3 / 2.5003405291834646 per mil
38 temperament / 17/5 / 2.3768516261347683 per mil
38 temperament / 17/9 / 3.514791770920289 per mil


39 temperament / 3 / 4.781089022433682 per mil
39 temperament / 4 / 0.0 per mil
39 temperament / 5 / 11.405238445971133 per mil
39 temperament / 6 / 4.781089022433682 per mil
39 temperament / 7 / 12.483127185809352 per mil
39 temperament / 8 / 0.0 per mil
39 temperament / 9 / 9.562178044867336 per mil
39 temperament / 10 / 11.405238445971133 per mil
39 temperament / 11 / 2.106842901164252 per mil
39 temperament / 12 / 4.781089022433682 per mil
39 temperament / 13 / 8.132025833399892 per mil
39 temperament / 14 / 12.483127185809352 per mil
39 temperament / 15 / 9.454698172621235 per mil
39 temperament / 16 / 0.0 per mil
39 temperament / 17 / 10.53976432726217 per mil
39 temperament / 18 / 9.562178044867336 per mil
39 temperament / 5/3 / 6.624149423537395 per mil
39 temperament / 7/3 / 8.376809432782684 per mil
39 temperament / 11/3 / 2.674246121269208 per mil
39 temperament / 11/5 / 9.298395544806937 per mil
39 temperament / 13/3 / 12.727910785192531 per mil
39 temperament / 13/5 / 6.103761361654858 per mil
39 temperament / 13/9 / 7.946821762758627 per mil
39 temperament / 17/3 / 10.32017229132931 per mil
39 temperament / 17/5 / 3.696022867792359 per mil
39 temperament / 17/9 / 5.539083268896072 per mil


40 temperament / 3 / 9.96250072115612 per mil
40 temperament / 4 / 0.0 per mil
40 temperament / 5 / 3.0719051126378294 per mil
40 temperament / 6 / 9.96250072115612 per mil
40 temperament / 7 / 7.35492205760413 per mil
40 temperament / 8 / 0.0 per mil
40 temperament / 9 / 5.074998557687838 per mil
40 temperament / 10 / 3.0719051126378294 per mil
40 temperament / 11 / 9.431618637297301 per mil
40 temperament / 12 / 9.96250072115612 per mil
40 temperament / 13 / 0.43971814109222684 per mil
40 temperament / 14 / 7.35492205760413 per mil
40 temperament / 15 / 6.890595608518679 per mil
40 temperament / 16 / 0.0 per mil
40 temperament / 17 / 12.4628412503391 per mil
40 temperament / 18 / 5.074998557687838 per mil
40 temperament / 5/3 / 11.96559416620624 per mil
40 temperament / 7/3 / 2.607578663551907 per mil
40 temperament / 11/3 / 0.5308820838589856 per mil
40 temperament / 11/5 / 12.496476250064864 per mil
40 temperament / 13/3 / 9.522782580064337 per mil
40 temperament / 13/5 / 3.5116232537297787 per mil
40 temperament / 13/9 / 5.514716698779787 per mil
40 temperament / 17/3 / 2.5003405291834646 per mil
40 temperament / 17/5 / 9.465253637023107 per mil
40 temperament / 17/9 / 7.4621601919729885 per mil


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


42 temperament / 3 / 10.275594516939158 per mil
42 temperament / 4 / 0.0 per mil
42 temperament / 5 / 11.405238445971133 per mil
42 temperament / 6 / 10.275594516939158 per mil
42 temperament / 7 / 2.1688874662053603 per mil
42 temperament / 8 / 0.0 per mil
42 temperament / 9 / 3.258334775645494 per mil
42 temperament / 10 / 11.405238445971133 per mil
42 temperament / 11 / 7.050666256344929 per mil
42 temperament / 12 / 10.275594516939158 per mil
42 temperament / 13 / 9.963527664901717 per mil
42 temperament / 14 / 2.1688874662053603 per mil
42 temperament / 15 / 2.1286908466139343 per mil
42 temperament / 16 / 0.0 per mil
42 temperament / 17 / 7.775253987756137 per mil
42 temperament / 18 / 3.258334775645494 per mil
42 temperament / 5/3 / 1.1296439290319205 per mil
42 temperament / 7/3 / 8.106707050733824 per mil
42 temperament / 11/3 / 6.483263036239917 per mil
42 temperament / 11/5 / 5.353619107207718 per mil
42 temperament / 13/3 / 3.5704016276833785 per mil
42 temperament / 13/5 / 2.4407576986511526 per mil
42 temperament / 13/9 / 6.705192889255973 per mil
42 temperament / 17/3 / 2.5003405291834646 per mil
42 temperament / 17/5 / 3.629984458215052 per mil
42 temperament / 17/9 / 11.033588763401546 per mil


43 temperament / 3 / 3.5671518839467398 per mil
43 temperament / 4 / 0.0 per mil
43 temperament / 5 / 3.653300461475051 per mil
43 temperament / 6 / 3.5671518839467398 per mil
43 temperament / 7 / 6.598566314488852 per mil
43 temperament / 8 / 0.0 per mil
43 temperament / 9 / 7.134303767893535 per mil
43 temperament / 10 / 3.653300461475051 per mil
43 temperament / 11 / 5.684660432470123 per mil
43 temperament / 12 / 3.5671518839467398 per mil
43 temperament / 13 / 2.7652995364410016 per mil
43 temperament / 14 / 6.598566314488852 per mil
43 temperament / 15 / 0.08614857752775595 per mil
43 temperament / 16 / 0.0 per mil
43 temperament / 17 / 5.5604145636143905 per mil
43 temperament / 18 / 7.134303767893535 per mil
43 temperament / 5/3 / 7.22045234542168 per mil
43 temperament / 7/3 / 10.16571819843562 per mil
43 temperament / 11/3 / 9.25181231641714 per mil
43 temperament / 11/5 / 2.0313599709951005 per mil
43 temperament / 13/3 / 0.8018523475061962 per mil
43 temperament / 13/5 / 6.41859999791583 per mil
43 temperament / 13/9 / 4.3690042314527 per mil
43 temperament / 17/3 / 9.127566447560742 per mil
43 temperament / 17/5 / 1.9071141021393956 per mil
43 temperament / 17/9 / 10.561095621980598 per mil


44 temperament / 3 / 5.946590187934864 per mil
44 temperament / 4 / 0.0 per mil
44 temperament / 5 / 3.746276705544005 per mil
44 temperament / 6 / 5.946590187934864 per mil
44 temperament / 7 / 10.82689612421406 per mil
44 temperament / 8 / 0.0 per mil
44 temperament / 9 / 10.834092351403063 per mil
44 temperament / 10 / 3.746276705544005 per mil
44 temperament / 11 / 4.886164091842781 per mil
44 temperament / 12 / 5.946590187934864 per mil
44 temperament / 13 / 4.105736404362403 per mil
44 temperament / 14 / 10.82689612421406 per mil
44 temperament / 15 / 2.200313482390359 per mil
44 temperament / 16 / 0.0 per mil
44 temperament / 17 / 3.4462496587518157 per mil
44 temperament / 18 / 10.834092351403063 per mil
44 temperament / 5/3 / 9.692866893478925 per mil
44 temperament / 7/3 / 4.880305936279167 per mil
44 temperament / 11/3 / 10.832754279777369 per mil
44 temperament / 11/5 / 1.1398873862987768 per mil
44 temperament / 13/3 / 1.84085378357203 per mil
44 temperament / 13/5 / 7.852013109906575 per mil
44 temperament / 13/9 / 7.787443971507102 per mil
44 temperament / 17/3 / 2.5003405291834646 per mil
44 temperament / 17/5 / 7.192526364295793 per mil
44 temperament / 17/9 / 8.446930717117995 per mil


45 temperament / 3 / 7.184722943378352 per mil
45 temperament / 4 / 0.0 per mil
45 temperament / 5 / 10.816983776251066 per mil
45 temperament / 6 / 7.184722943378352 per mil
45 temperament / 7 / 7.35492205760413 per mil
45 temperament / 8 / 0.0 per mil
45 temperament / 9 / 7.8527763354656335 per mil
45 temperament / 10 / 10.816983776251066 per mil
45 temperament / 11 / 7.235048029369362 per mil
45 temperament / 12 / 7.184722943378352 per mil
45 temperament / 13 / 10.671392970018957 per mil
45 temperament / 14 / 7.35492205760413 per mil
45 temperament / 15 / 4.220515502592392 per mil
45 temperament / 16 / 0.0 per mil
45 temperament / 17 / 1.4260476385497962 per mil
45 temperament / 18 / 7.8527763354656335 per mil
45 temperament / 5/3 / 3.6322608328729356 per mil
45 temperament / 7/3 / 0.17019911422588851 per mil
45 temperament / 11/3 / 7.802451249474318 per mil
45 temperament / 11/5 / 4.170190416601799 per mil
45 temperament / 13/3 / 4.366106308824557 per mil
45 temperament / 13/5 / 0.7338454759520108 per mil
45 temperament / 13/9 / 2.818616634553517 per mil
45 temperament / 17/3 / 8.610770581927607 per mil
45 temperament / 17/5 / 9.979190807421379 per mil
45 temperament / 17/9 / 6.426728696915962 per mil


46 temperament / 3 / 1.9940210179744122 per mil
46 temperament / 4 / 0.0 per mil
46 temperament / 5 / 4.1588616343769536 per mil
46 temperament / 6 / 1.9940210179744122 per mil
46 temperament / 7 / 3.007095970647633 per mil
46 temperament / 8 / 0.0 per mil
46 temperament / 9 / 3.9880420359487134 per mil
46 temperament / 10 / 4.1588616343769536 per mil
46 temperament / 11 / 2.909879506862556 per mil
46 temperament / 12 / 1.9940210179744122 per mil
46 temperament / 13 / 4.7875442280487235 per mil
46 temperament / 14 / 3.007095970647633 per mil
46 temperament / 15 / 6.152882652350811 per mil
46 temperament / 16 / 0.0 per mil
46 temperament / 17 / 0.5063195112086638 per mil
46 temperament / 18 / 3.9880420359487134 per mil
46 temperament / 5/3 / 2.1648406164024303 per mil
46 temperament / 7/3 / 5.001116988622018 per mil
46 temperament / 11/3 / 4.903900524836691 per mil
46 temperament / 11/5 / 7.068741141239482 per mil
46 temperament / 13/3 / 6.781565246022622 per mil
46 temperament / 13/5 / 8.946405862425454 per mil
46 temperament / 13/9 / 8.775586263997216 per mil
46 temperament / 17/3 / 2.5003405291834646 per mil
46 temperament / 17/5 / 4.665181145585562 per mil
46 temperament / 17/9 / 4.494361547157544 per mil


47 temperament / 3 / 10.494415614773045 per mil
47 temperament / 4 / 0.0 per mil
47 temperament / 5 / 2.779158717149399 per mil
47 temperament / 6 / 10.494415614773045 per mil
47 temperament / 7 / 1.155716240268112 per mil
47 temperament / 8 / 0.0 per mil
47 temperament / 9 / 0.28776451513465306 per mil
47 temperament / 10 / 2.779158717149399 per mil
47 temperament / 11 / 8.65348774568142 per mil
47 temperament / 12 / 10.494415614773045 per mil
47 temperament / 13 / 1.6879414333759168 per mil
47 temperament / 14 / 1.155716240268112 per mil
47 temperament / 15 / 8.003021412757882 per mil
47 temperament / 16 / 0.0 per mil
47 temperament / 17 / 2.356458271615694 per mil
47 temperament / 18 / 0.28776451513465306 per mil
47 temperament / 5/3 / 7.715256897623535 per mil
47 temperament / 7/3 / 9.626463889639586 per mil
47 temperament / 11/3 / 2.128692384226083 per mil
47 temperament / 11/5 / 9.843949281850033 per mil
47 temperament / 13/3 / 9.094238696531406 per mil
47 temperament / 13/5 / 4.467100150525538 per mil
47 temperament / 13/9 / 1.400176918241458 per mil
47 temperament / 17/3 / 8.13795734315692 per mil
47 temperament / 17/5 / 0.4227004455337191 per mil
47 temperament / 17/9 / 2.644222786750472 per mil


48 temperament / 3 / 1.6291673878227053 per mil
48 temperament / 4 / 0.0 per mil
48 temperament / 5 / 9.428094887362182 per mil
48 temperament / 6 / 1.6291673878227053 per mil
48 temperament / 7 / 5.145077942395826 per mil
48 temperament / 8 / 0.0 per mil
48 temperament / 9 / 3.258334775645494 per mil
48 temperament / 10 / 9.428094887362182 per mil
48 temperament / 11 / 1.0982853039639973 per mil
48 temperament / 12 / 1.6291673878227053 per mil
48 temperament / 13 / 7.893615192241188 per mil
48 temperament / 14 / 5.145077942395826 per mil
48 temperament / 15 / 9.776071058147927 per mil
48 temperament / 16 / 0.0 per mil
48 temperament / 17 / 4.129507917005768 per mil
48 temperament / 18 / 3.258334775645494 per mil
48 temperament / 5/3 / 7.798927499539587 per mil
48 temperament / 7/3 / 6.774245330218559 per mil
48 temperament / 11/3 / 0.5308820838589856 per mil
48 temperament / 11/5 / 8.329809583398212 per mil
48 temperament / 13/3 / 9.522782580064337 per mil
48 temperament / 13/5 / 3.5116232537297787 per mil
48 temperament / 13/9 / 9.68138336544644 per mil
48 temperament / 17/3 / 2.5003405291834646 per mil
48 temperament / 17/5 / 5.298586970356456 per mil
48 temperament / 17/9 / 0.8711731413604262 per mil


49 temperament / 3 / 6.874233972721466 per mil
49 temperament / 4 / 0.0 per mil
49 temperament / 5 / 4.602517357535751 per mil
49 temperament / 6 / 6.874233972721466 per mil
49 temperament / 7 / 8.971608554640742 per mil
49 temperament / 8 / 0.0 per mil
49 temperament / 9 / 6.659695319863185 per mil
49 temperament / 10 / 4.602517357535751 per mil
49 temperament / 11 / 9.956136464743526 per mil
49 temperament / 12 / 6.874233972721466 per mil
49 temperament / 13 / 6.562167120684026 per mil
49 temperament / 14 / 8.971608554640742 per mil
49 temperament / 15 / 8.931411935049315 per mil
49 temperament / 16 / 0.0 per mil
49 temperament / 17 / 5.830188189114613 per mil
49 temperament / 18 / 6.659695319863185 per mil
49 temperament / 5/3 / 2.2717166151857704 per mil
49 temperament / 7/3 / 2.097374581919248 per mil
49 temperament / 11/3 / 3.081902492022226 per mil
49 temperament / 11/5 / 5.353619107207718 per mil
49 temperament / 13/3 / 6.971762171901069 per mil
49 temperament / 13/5 / 9.243478787086534 per mil
49 temperament / 13/9 / 0.09752819917940858 per mil
49 temperament / 17/3 / 7.703741103469608 per mil
49 temperament / 17/5 / 9.975457718655711 per mil
49 temperament / 17/9 / 0.8295071307484747 per mil


50 temperament / 3 / 4.962500721156116 per mil
50 temperament / 4 / 0.0 per mil
50 temperament / 5 / 1.928094887362175 per mil
50 temperament / 6 / 4.962500721156116 per mil
50 temperament / 7 / 7.35492205760413 per mil
50 temperament / 8 / 0.0 per mil
50 temperament / 9 / 9.925001442312148 per mil
50 temperament / 10 / 1.928094887362175 per mil
50 temperament / 11 / 0.5683813627027079 per mil
50 temperament / 12 / 4.962500721156116 per mil
50 temperament / 13 / 0.43971814109222684 per mil
50 temperament / 14 / 7.35492205760413 per mil
50 temperament / 15 / 6.890595608518679 per mil
50 temperament / 16 / 0.0 per mil
50 temperament / 17 / 7.462841250339094 per mil
50 temperament / 18 / 9.925001442312148 per mil
50 temperament / 5/3 / 3.034405833793774 per mil
50 temperament / 7/3 / 2.3924213364480975 per mil
50 temperament / 11/3 / 5.53088208385899 per mil
50 temperament / 11/5 / 2.496476250064883 per mil
50 temperament / 13/3 / 4.522782580064333 per mil
50 temperament / 13/5 / 1.4883767462702258 per mil
50 temperament / 13/9 / 9.485283301220226 per mil
50 temperament / 17/3 / 2.5003405291834646 per mil
50 temperament / 17/5 / 5.534746362976906 per mil
50 temperament / 17/9 / 2.462160191972984 per mil


51 temperament / 3 / 3.2727933964910028 per mil
51 temperament / 4 / 0.0 per mil
51 temperament / 5 / 8.202604691283755 per mil
51 temperament / 6 / 3.2727933964910028 per mil
51 temperament / 7 / 3.433353430153163 per mil
51 temperament / 8 / 0.0 per mil
51 temperament / 9 / 6.545586792981978 per mil
51 temperament / 10 / 8.202604691283755 per mil
51 temperament / 11 / 8.45122648043456 per mil
51 temperament / 12 / 3.2727933964910028 per mil
51 temperament / 13 / 5.442634800084334 per mil
51 temperament / 14 / 3.433353430153163 per mil
51 temperament / 15 / 4.929811294793196 per mil
51 temperament / 16 / 0.0 per mil
51 temperament / 17 / 9.03146870131949 per mil
51 temperament / 18 / 6.545586792981978 per mil
51 temperament / 5/3 / 8.132445049480076 per mil
51 temperament / 7/3 / 6.706146826644166 per mil
51 temperament / 11/3 / 7.883823260329548 per mil
51 temperament / 11/5 / 0.24862178915080468 per mil
51 temperament / 13/3 / 2.1698414035937477 per mil
51 temperament / 13/5 / 5.962603645886633 per mil
51 temperament / 13/9 / 1.1029519928974496 per mil
51 temperament / 17/3 / 7.3035810394439515 per mil
51 temperament / 17/5 / 0.8288640100357902 per mil
51 temperament / 17/9 / 4.030787642953282 per mil


52 temperament / 3 / 8.039423798079204 per mil
52 temperament / 4 / 0.0 per mil
52 temperament / 5 / 4.994982035714745 per mil
52 temperament / 6 / 8.039423798079204 per mil
52 temperament / 7 / 0.33738563470353533 per mil
52 temperament / 8 / 0.0 per mil
52 temperament / 9 / 3.1519216346109213 per mil
52 temperament / 10 / 4.994982035714745 per mil
52 temperament / 11 / 2.106842901164252 per mil
52 temperament / 12 / 8.039423798079204 per mil
52 temperament / 13 / 8.132025833399892 per mil
52 temperament / 14 / 0.33738563470353533 per mil
52 temperament / 15 / 3.0444417623648468 per mil
52 temperament / 16 / 0.0 per mil
52 temperament / 17 / 8.691004903507062 per mil
52 temperament / 18 / 3.1519216346109213 per mil
52 temperament / 5/3 / 6.1963633969754905 per mil
52 temperament / 7/3 / 8.376809432782684 per mil
52 temperament / 11/3 / 9.084502531525596 per mil
52 temperament / 11/5 / 2.8881391345505216 per mil
52 temperament / 13/3 / 0.09260203532027167 per mil
52 temperament / 13/5 / 6.103761361654858 per mil
52 temperament / 13/9 / 7.946821762758627 per mil
52 temperament / 17/3 / 2.5003405291834646 per mil
52 temperament / 17/5 / 3.696022867792359 per mil
52 temperament / 17/9 / 5.539083268896072 per mil


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


54 temperament / 3 / 7.630091871436484 per mil
54 temperament / 4 / 0.0 per mil
54 temperament / 5 / 7.113280072547356 per mil
54 temperament / 6 / 7.630091871436484 per mil
54 temperament / 7 / 7.4598927572105955 per mil
54 temperament / 8 / 0.0 per mil
54 temperament / 9 / 3.258334775645494 per mil
54 temperament / 10 / 7.113280072547356 per mil
54 temperament / 11 / 3.531344325665653 per mil
54 temperament / 12 / 7.630091871436484 per mil
54 temperament / 13 / 3.2639855626115377 per mil
54 temperament / 14 / 7.4598927572105955 per mil
54 temperament / 15 / 0.5168117988887388 per mil
54 temperament / 16 / 0.0 per mil
54 temperament / 17 / 5.129751342253491 per mil
54 temperament / 18 / 3.258334775645494 per mil
54 temperament / 5/3 / 3.7751465745344825 per mil
54 temperament / 7/3 / 0.17019911422588851 per mil
54 temperament / 11/3 / 4.098747545770665 per mil
54 temperament / 11/5 / 7.873894120305508 per mil
54 temperament / 13/3 / 4.366106308824557 per mil
54 temperament / 13/5 / 8.141252883359428 per mil
54 temperament / 13/9 / 6.522320338257281 per mil
54 temperament / 17/3 / 2.5003405291834646 per mil
54 temperament / 17/5 / 6.275487103717614 per mil
54 temperament / 17/9 / 8.388086117898874 per mil


55 temperament / 3 / 3.1443189029742857 per mil
55 temperament / 4 / 0.0 per mil
55 temperament / 5 / 5.344632385365089 per mil
55 temperament / 6 / 3.1443189029742857 per mil
55 temperament / 7 / 7.35492205760413 per mil
55 temperament / 8 / 0.0 per mil
55 temperament / 9 / 6.288637805948516 per mil
55 temperament / 10 / 5.344632385365089 per mil
55 temperament / 11 / 4.886164091842781 per mil
55 temperament / 12 / 3.1443189029742857 per mil
55 temperament / 13 / 8.651190949816922 per mil
55 temperament / 14 / 7.35492205760413 per mil
55 temperament / 15 / 2.200313482390359 per mil
55 temperament / 16 / 0.0 per mil
55 temperament / 17 / 3.4462496587518157 per mil
55 temperament / 18 / 6.288637805948516 per mil
55 temperament / 5/3 / 8.488951288339264 per mil
55 temperament / 7/3 / 4.210603154629927 per mil
55 temperament / 11/3 / 1.7418451888683295 per mil
55 temperament / 11/5 / 7.9510217046103175 per mil
55 temperament / 13/3 / 6.386308329026577 per mil
55 temperament / 13/5 / 3.3065585644520556 per mil
55 temperament / 13/9 / 3.241989426052583 per mil
55 temperament / 17/3 / 6.590568561725574 per mil
55 temperament / 17/5 / 1.8983827266132458 per mil
55 temperament / 17/9 / 8.446930717117995 per mil


56 temperament / 3 / 4.323213564558226 per mil
56 temperament / 4 / 0.0 per mil
56 temperament / 5 / 0.49952345879072935 per mil
56 temperament / 6 / 4.323213564558226 per mil
56 temperament / 7 / 3.783493486175571 per mil
56 temperament / 8 / 0.0 per mil
56 temperament / 9 / 8.646427129116423 per mil
56 temperament / 10 / 0.49952345879072935 per mil
56 temperament / 11 / 4.8540956484169895 per mil
56 temperament / 12 / 4.323213564558226 per mil
56 temperament / 13 / 4.011146712520786 per mil
56 temperament / 14 / 3.783493486175571 per mil
56 temperament / 15 / 3.823690105766997 per mil
56 temperament / 16 / 0.0 per mil
56 temperament / 17 / 1.8228730353751916 per mil
56 temperament / 18 / 8.646427129116423 per mil
56 temperament / 5/3 / 4.822737023349122 per mil
56 temperament / 7/3 / 8.106707050733824 per mil
56 temperament / 11/3 / 0.5308820838589856 per mil
56 temperament / 11/5 / 5.353619107207718 per mil
56 temperament / 13/3 / 8.334360277078526 per mil
56 temperament / 13/5 / 3.5116232537297787 per mil
56 temperament / 13/9 / 5.199569015505889 per mil
56 temperament / 17/3 / 2.5003405291834646 per mil
56 temperament / 17/5 / 2.3223964941659903 per mil
56 temperament / 17/9 / 6.8235540937413575 per mil


57 temperament / 3 / 6.015132300103421 per mil
57 temperament / 4 / 0.0 per mil
57 temperament / 5 / 6.138621203151673 per mil
57 temperament / 6 / 6.015132300103421 per mil
57 temperament / 7 / 0.33737819795509605 per mil
57 temperament / 8 / 0.0 per mil
57 temperament / 9 / 5.513595048915909 per mil
57 temperament / 10 / 6.138621203151673 per mil
57 temperament / 11 / 3.291267760104355 per mil
57 temperament / 12 / 6.015132300103421 per mil
57 temperament / 13 / 1.3146678238200593 per mil
57 temperament / 14 / 0.33737819795509605 per mil
57 temperament / 15 / 5.390106145867213 per mil
57 temperament / 16 / 0.0 per mil
57 temperament / 17 / 0.25645699527493404 per mil
57 temperament / 18 / 5.513595048915909 per mil
57 temperament / 5/3 / 0.12348890304836324 per mil
57 temperament / 7/3 / 5.677754102148381 per mil
57 temperament / 11/3 / 2.723864539999288 per mil
57 temperament / 11/5 / 2.847353443047318 per mil
57 temperament / 13/3 / 7.329800123923979 per mil
57 temperament / 13/5 / 7.453289026971954 per mil
57 temperament / 13/9 / 4.198927225095628 per mil
57 temperament / 17/3 / 6.271589295377966 per mil
57 temperament / 17/5 / 6.3950781984265515 per mil
57 temperament / 17/9 / 5.257138053641142 per mil


58 temperament / 3 / 1.2443958305680125 per mil
58 temperament / 4 / 0.0 per mil
58 temperament / 5 / 5.658112009189531 per mil
58 temperament / 6 / 1.2443958305680125 per mil
58 temperament / 7 / 2.9899055286026766 per mil
58 temperament / 8 / 0.0 per mil
58 temperament / 9 / 2.488791661136136 per mil
58 temperament / 10 / 5.658112009189531 per mil
58 temperament / 11 / 6.085622742013019 per mil
58 temperament / 12 / 1.2443958305680125 per mil
58 temperament / 13 / 6.456833583045718 per mil
58 temperament / 14 / 2.9899055286026766 per mil
58 temperament / 15 / 6.90250783975721 per mil
58 temperament / 16 / 0.0 per mil
58 temperament / 17 / 1.2559446986149525 per mil
58 temperament / 18 / 2.488791661136136 per mil
58 temperament / 5/3 / 4.413716178621407 per mil
58 temperament / 7/3 / 1.745509698034664 per mil
58 temperament / 11/3 / 4.841226911445173 per mil
58 temperament / 11/5 / 0.4275107328234884 per mil
58 temperament / 13/3 / 5.212437752478135 per mil
58 temperament / 13/5 / 0.7987215738564091 per mil
58 temperament / 13/9 / 3.968041921909804 per mil
58 temperament / 17/3 / 2.5003405291834646 per mil
58 temperament / 17/5 / 6.914056707804539 per mil
58 temperament / 17/9 / 3.744736359751144 per mil


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


60 temperament / 3 / 1.6291673878227053 per mil
60 temperament / 4 / 0.0 per mil
60 temperament / 5 / 5.26142822069553 per mil
60 temperament / 6 / 1.6291673878227053 per mil
60 temperament / 7 / 7.35492205760413 per mil
60 temperament / 8 / 0.0 per mil
60 temperament / 9 / 3.258334775645494 per mil
60 temperament / 10 / 5.26142822069553 per mil
60 temperament / 11 / 7.235048029369362 per mil
60 temperament / 12 / 1.6291673878227053 per mil
60 temperament / 13 / 0.43971814109222684 per mil
60 temperament / 14 / 7.35492205760413 per mil
60 temperament / 15 / 6.890595608518679 per mil
60 temperament / 16 / 0.0 per mil
60 temperament / 17 / 4.129507917005768 per mil
60 temperament / 18 / 3.258334775645494 per mil
60 temperament / 5/3 / 3.6322608328729356 per mil
60 temperament / 7/3 / 5.725754669781424 per mil
60 temperament / 11/3 / 7.802451249474318 per mil
60 temperament / 11/5 / 4.170190416601799 per mil
60 temperament / 13/3 / 1.1894492467310058 per mil
60 temperament / 13/5 / 4.82171007960358 per mil
60 temperament / 13/9 / 2.818616634553517 per mil
60 temperament / 17/3 / 2.5003405291834646 per mil
60 temperament / 17/5 / 1.131920303689804 per mil
60 temperament / 17/9 / 0.8711731413604262 per mil


61 temperament / 3 / 5.201433705073422 per mil
61 temperament / 4 / 0.0 per mil
61 temperament / 5 / 5.940757571654187 per mil
61 temperament / 6 / 5.201433705073422 per mil
61 temperament / 7 / 4.0762335330140065 per mil
61 temperament / 8 / 0.0 per mil
61 temperament / 9 / 5.990575212803967 per mil
61 temperament / 10 / 5.940757571654187 per mil
61 temperament / 11 / 0.41522519467435126 per mil
61 temperament / 12 / 5.201433705073422 per mil
61 temperament / 13 / 4.478314645793069 per mil
61 temperament / 14 / 4.0762335330140065 per mil
61 temperament / 15 / 5.251251346223618 per mil
61 temperament / 16 / 0.0 per mil
61 temperament / 17 / 5.495628135585004 per mil
61 temperament / 18 / 5.990575212803967 per mil
61 temperament / 5/3 / 0.73932386658071 per mil
61 temperament / 7/3 / 7.115775384863382 per mil
61 temperament / 11/3 / 5.616658899747606 per mil
61 temperament / 11/5 / 6.355982766328566 per mil
61 temperament / 13/3 / 0.7231190592799225 per mil
61 temperament / 13/5 / 1.4624429258609517 per mil
61 temperament / 13/9 / 5.924552764353552 per mil
61 temperament / 17/3 / 5.696380782291954 per mil
61 temperament / 17/5 / 4.957056915711577 per mil
61 temperament / 17/9 / 0.49494707721886577 per mil


62 temperament / 3 / 4.317339430833456 per mil
62 temperament / 4 / 0.0 per mil
62 temperament / 5 / 0.6525502739281319 per mil
62 temperament / 6 / 4.317339430833456 per mil
62 temperament / 7 / 0.9033091543784177 per mil
62 temperament / 8 / 0.0 per mil
62 temperament / 9 / 7.4943533963975355 per mil
62 temperament / 10 / 0.6525502739281319 per mil
62 temperament / 11 / 7.818715411490873 per mil
62 temperament / 12 / 4.317339430833456 per mil
62 temperament / 13 / 6.891331044317939 per mil
62 temperament / 14 / 0.9033091543784177 per mil
62 temperament / 15 / 3.6647891569058233 per mil
62 temperament / 16 / 0.0 per mil
62 temperament / 17 / 6.817679960016518 per mil
62 temperament / 18 / 7.4943533963975355 per mil
62 temperament / 5/3 / 4.969889704761532 per mil
62 temperament / 7/3 / 3.4140302764551214 per mil
62 temperament / 11/3 / 3.50137598065714 per mil
62 temperament / 11/5 / 7.657766572645524 per mil
62 temperament / 13/3 / 2.573991613484053 per mil
62 temperament / 13/5 / 7.543881318245904 per mil
62 temperament / 13/9 / 1.7433478173491945 per mil
62 temperament / 17/3 / 2.5003405291834646 per mil
62 temperament / 17/5 / 7.470230233944664 per mil
62 temperament / 17/9 / 1.816998901650324 per mil


63 temperament / 3 / 2.339086580431249 per mil
63 temperament / 4 / 0.0 per mil
63 temperament / 5 / 4.467777427044739 per mil
63 temperament / 6 / 2.339086580431249 per mil
63 temperament / 7 / 2.1688874662053603 per mil
63 temperament / 8 / 0.0 per mil
63 temperament / 9 / 4.678173160862443 per mil
63 temperament / 10 / 4.467777427044739 per mil
63 temperament / 11 / 0.8858416801629798 per mil
63 temperament / 12 / 2.339086580431249 per mil
63 temperament / 13 / 2.0270197283938085 per mil
63 temperament / 14 / 2.1688874662053603 per mil
63 temperament / 15 / 2.1286908466139343 per mil
63 temperament / 16 / 0.0 per mil
63 temperament / 17 / 7.775253987756137 per mil
63 temperament / 18 / 4.678173160862443 per mil
63 temperament / 5/3 / 6.806864007476099 per mil
63 temperament / 7/3 / 0.17019911422588851 per mil
63 temperament / 11/3 / 1.4532449002679915 per mil
63 temperament / 11/5 / 5.353619107207718 per mil
63 temperament / 13/3 / 4.366106308824557 per mil
63 temperament / 13/5 / 2.4407576986511526 per mil
63 temperament / 13/9 / 6.705192889255973 per mil
63 temperament / 17/3 / 5.436167407324444 per mil
63 temperament / 17/5 / 3.629984458215052 per mil
63 temperament / 17/9 / 3.097080826893528 per mil


64 temperament / 3 / 6.837500721156076 per mil
64 temperament / 4 / 0.0 per mil
64 temperament / 5 / 6.196905112637818 per mil
64 temperament / 6 / 6.837500721156076 per mil
64 temperament / 7 / 5.145077942395826 per mil
64 temperament / 8 / 0.0 per mil
64 temperament / 9 / 1.9499985576878487 per mil
64 temperament / 10 / 6.196905112637818 per mil
64 temperament / 11 / 6.306618637297312 per mil
64 temperament / 12 / 6.837500721156076 per mil
64 temperament / 13 / 2.6852818589078176 per mil
64 temperament / 14 / 5.145077942395826 per mil
64 temperament / 15 / 0.6405956085187015 per mil
64 temperament / 16 / 0.0 per mil
64 temperament / 17 / 6.287158749660904 per mil
64 temperament / 18 / 1.9499985576878487 per mil
64 temperament / 5/3 / 2.590594166206217 per mil
64 temperament / 7/3 / 3.6424213364480984 per mil
64 temperament / 11/3 / 0.5308820838589856 per mil
64 temperament / 11/5 / 3.1214762500648696 per mil
64 temperament / 13/3 / 6.102217419935663 per mil
64 temperament / 13/5 / 3.5116232537297787 per mil
64 temperament / 13/9 / 0.7352833012201909 per mil
64 temperament / 17/3 / 2.5003405291834646 per mil
64 temperament / 17/5 / 0.09025363702308553 per mil
64 temperament / 17/9 / 4.337160191972944 per mil


65 temperament / 3 / 0.3471161057714278 per mil
65 temperament / 4 / 0.0 per mil
65 temperament / 5 / 1.1488281895609131 per mil
65 temperament / 6 / 0.3471161057714278 per mil
65 temperament / 7 / 7.35492205760413 per mil
65 temperament / 8 / 0.0 per mil
65 temperament / 9 / 0.6942322115429111 per mil
65 temperament / 10 / 1.1488281895609131 per mil
65 temperament / 11 / 2.106842901164252 per mil
65 temperament / 12 / 0.3471161057714278 per mil
65 temperament / 13 / 7.252589551215549 per mil
65 temperament / 14 / 7.35492205760413 per mil
65 temperament / 15 / 0.8017120837889857 per mil
65 temperament / 16 / 0.0 per mil
65 temperament / 17 / 4.844851057353217 per mil
65 temperament / 18 / 0.6942322115429111 per mil
65 temperament / 5/3 / 1.4959442953322855 per mil
65 temperament / 7/3 / 7.007805951832702 per mil
65 temperament / 11/3 / 2.453959006935902 per mil
65 temperament / 11/5 / 0.9580147116033388 per mil
65 temperament / 13/3 / 7.599705656987421 per mil
65 temperament / 13/5 / 6.103761361654858 per mil
65 temperament / 13/9 / 7.437793621856703 per mil
65 temperament / 17/3 / 5.1919671631242 per mil
65 temperament / 17/5 / 3.696022867792359 per mil
65 temperament / 17/9 / 5.539083268896072 per mil


66 temperament / 3 / 5.946590187934864 per mil
66 temperament / 4 / 0.0 per mil
66 temperament / 5 / 3.746276705544005 per mil
66 temperament / 6 / 5.946590187934864 per mil
66 temperament / 7 / 4.324619027301191 per mil
66 temperament / 8 / 0.0 per mil
66 temperament / 9 / 3.258334775645494 per mil
66 temperament / 10 / 3.746276705544005 per mil
66 temperament / 11 / 4.886164091842781 per mil
66 temperament / 12 / 5.946590187934864 per mil
66 temperament / 13 / 3.4700211713951656 per mil
66 temperament / 14 / 4.324619027301191 per mil
66 temperament / 15 / 2.200313482390359 per mil
66 temperament / 16 / 0.0 per mil
66 temperament / 17 / 3.4462496587518157 per mil
66 temperament / 18 / 3.258334775645494 per mil
66 temperament / 5/3 / 5.458648258036214 per mil
66 temperament / 7/3 / 4.880305936279167 per mil
66 temperament / 11/3 / 4.31876087173777 per mil
66 temperament / 11/5 / 1.1398873862987768 per mil
66 temperament / 13/3 / 5.734903792185553 per mil
66 temperament / 13/5 / 0.27625553414900583 per mil
66 temperament / 13/9 / 0.21168639574953296 per mil
66 temperament / 17/3 / 2.5003405291834646 per mil
66 temperament / 17/5 / 7.192526364295793 per mil
66 temperament / 17/9 / 6.704584434397143 per mil


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