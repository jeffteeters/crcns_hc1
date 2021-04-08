# crcns_hc1

This repository contains a python script, `crt.py`, which calculates
the recording time for cells in the hc-1 dataset at https://CRCNS.org.

The scrpt requires a local directory called `data_size_info` which
contains a file named `datfiles.txt` that contains the names and sizes
and locations of all ".dat" files in the dataset; and a directory
named "xmlnrs" that contains the ".xml" and ".nrs" files corresponding
to the ".dat" files.  The contents of the `data_size_info` directory
are in the `data_size_info.zip` file available in this repository.
It was created by using the `unzip -l` command to list files in the
zip files that contain the dataset files.

The script also requires that file `IntraExtra.xls` be in the local
dirctory.  That is available from CRCNS.org in the downloads for the
hc-1 data set.

An example run of the script and output is given below.

```
$ ls
IntraExtra.xls		data_size_info	README.md	crt.py

$ python crt.py

** crcns.org hc-1 dataset files

1. d11221
name	size	channels	samplingRate	minutes
d11221.001.dat	90000000	6		20000	6.25
d11221.002.dat	90000000	6		20000	6.25
d1122101.dat	38404096	8		10000	4.0
d1122102.dat	38404096	8		10000	4.0
d1122103.dat	38404096	8		10000	4.0
d1122104.dat	77987840	8		20000	4.06
d1122105.dat	77987840	8		20000	4.06
d1122106.dat	77987840	8		20000	4.06
d1122107.dat	77987840	8		20000	4.06
d1122108.dat	77987840	8		20000	4.06
d1122109.dat	77987840	8		20000	4.06
11 files, total time=48.87, number of channels inconsistent

2. d11222
name	size	channels	samplingRate	minutes
d11222.001.dat	180000000	6		20000	12.5
d11222.002.dat	180000000	6		20000	12.5
d1122202.dat	77987840	8		10000	8.12
d1122203.dat	77987840	8		10000	8.12
d1122204.dat	77987840	8		10000	8.12
d1122205.dat	77987840	8		10000	8.12
d1122206.dat	77987840	8		10000	8.12
d1122207.dat	77987840	8		10000	8.12
d1122208.dat	77987840	8		10000	8.12
d1122209.dat	77987840	8		10000	8.12
d1122210.dat	77987840	8		10000	8.12
d1122211.dat	77987840	8		10000	8.12
d1122212.dat	77987840	8		10000	8.12
d1122213.dat	77987840	8		10000	8.12
14 files, total time=122.48, number of channels inconsistent

3. d12821
name	size	channels	samplingRate	minutes
d12821.001.dat	180000000	6		20000	12.5
d12821.002.dat	2670000		6		20000	0.19
d1282101.dat	38404096	8		10000	4.0
d1282102.dat	38404096	8		10000	4.0
d1282103.dat	38404096	8		10000	4.0
d1282104.dat	38404096	8		10000	4.0
d1282105.dat	38404096	8		10000	4.0
d1282106.dat	38404096	8		10000	4.0
8 files, total time=36.69, number of channels inconsistent

4. d13521
name	size	channels	samplingRate	minutes
d1352102.dat	76808192	8		20000	4.0
1 files, total time=4.0

5. d13522
name	size	channels	samplingRate	minutes
d1352201.dat	76808192	8		20000	4.0
d1352202.dat	76808192	8		20000	4.0
d1352203.dat	76808192	8		20000	4.0
d1352204.dat	76808192	8		20000	4.0
d1352205.dat	76808192	8		20000	4.0
d1352206.dat	76808192	8		20000	4.0
d1352207.dat	76808192	8		20000	4.0
d1352208.dat	76808192	8		20000	4.0
d1352209.dat	76808192	8		20000	4.0
d1352210.dat	76808192	8		20000	4.0
d1352211.dat	76808192	8		20000	4.0
d1352212.dat	76808192	8		20000	4.0
d1352213.dat	76808192	8		20000	4.0
13 files, total time=52.01

6. d13711
name	size	channels	samplingRate	minutes
d1371101.dat	76808192	8		20000	4.0
d1371102.dat	38404096	8		10000	4.0
d1371103.dat	76808192	8		20000	4.0
d1371104.dat	76808192	8		20000	4.0
d1371105.dat	38404096	8		10000	4.0
5 files, total time=20.0

7. d13921
name	size	channels	samplingRate	minutes
d1392101.dat	38404096	8		10000	4.0
d1392102.dat	38404096	8		10000	4.0
2 files, total time=8.0

8. d14521
name	size	channels	samplingRate	minutes
d14521.001.dat	90000000	6		20000	6.25
d14521.002.dat	90000000	6		20000	6.25
2 files, total time=12.5
differing intraExtra values: recording time 10.0

9. d14531
name	size	channels	samplingRate	minutes
d1453101.dat	38404096	8		10000	4.0
d1453102.dat	38404096	8		10000	4.0
d1453103.dat	38404096	8		10000	4.0
d1453104.dat	38404096	8		10000	4.0
4 files, total time=16.0

10. d14921
name	size	channels	samplingRate	minutes
d14921.001.dat	180000000	6		20000	12.5
d1492102.dat	38404096	8		10000	4.0
d1492103.dat	38404096	8		10000	4.0
d1492104.dat	38404096	8		10000	4.0
d1492105.dat	38404096	8		10000	4.0
d1492106.dat	38404096	8		10000	4.0
6 files, total time=32.5, number of channels inconsistent
differing intraExtra values: recording time 66.0, #_of_files '1', nChannels 6

11. d15121
name	size	channels	samplingRate	minutes
d1512101.dat	38404096	8		10000	4.0
d1512102.dat	38404096	8		10000	4.0
d1512103.dat	38404096	8		10000	4.0
d1512104.dat	38404096	8		10000	4.0
4 files, total time=16.0

12. d15611
name	size	channels	samplingRate	minutes
d15611.001.dat	420000000	None		None	0.0
1 files, total time=0.0 (xml file missing)

13. d15711
name	size	channels	samplingRate	minutes
d15711.001.dat	420000000	14		20000	12.5
1 files, total time=12.5
differing intraExtra values: recording time 60.0

14. d15712
name	size	channels	samplingRate	minutes
d15712.002.dat	420000000	14		20000	12.5
d15712.003.dat	420000000	14		20000	12.5
d15712.001.dat	420000000	14		20000	12.5
3 files, total time=37.5
differing intraExtra values: recording time 80.0

15. d16311
name	size	channels	samplingRate	minutes
d16311.002.dat	420000000	14		20000	12.5
d16311.001.dat	420000000	14		20000	12.5
2 files, total time=25.0
differing intraExtra values: recording time 120.0

16. d16613
name	size	channels	samplingRate	minutes
d16613.001.dat	420000000	14		20000	12.5
1 files, total time=12.5
differing intraExtra values: recording time nan

17. d16811
name	size	channels	samplingRate	minutes
d16811.001.dat	420000000	None		None	0.0
1 files, total time=0.0 (xml file missing)

18. d17012
name	size	channels	samplingRate	minutes
d17012.002.dat	101780000	14		20000	3.03
d17012.001.dat	420000000	14		20000	12.5
2 files, total time=15.53
differing intraExtra values: recording time 10.0

19. d17013
name	size	channels	samplingRate	minutes
d17013.002.dat	420000000	14		20000	12.5
d17013.003.dat	420000000	14		20000	12.5
d17013.001.dat	420000000	14		20000	12.5
3 files, total time=37.5
differing intraExtra values: recording time 60.0

20. d17014
name	size	channels	samplingRate	minutes
d17014.001.dat	420000000	14		20000	12.5
1 files, total time=12.5
differing intraExtra values: recording time 66.0

21. d17111
name	size	channels	samplingRate	minutes
d17111.002.dat	420000000	14		20000	12.5
d17111.003.dat	420000000	14		20000	12.5
d17111.004.dat	420000000	14		20000	12.5
d17111.001.dat	420000000	14		20000	12.5
4 files, total time=50.0
differing intraExtra values: recording time 46.0

22. d17211
name	size	channels	samplingRate	minutes
d17211.002.dat	240000000	8		20000	12.5
d17211.001.dat	240000000	8		20000	12.5
2 files, total time=25.0
differing intraExtra values: recording time 36.0

23. d17212
name	size	channels	samplingRate	minutes
d17212.002.dat	240000000	8		20000	12.5
d17212.001.dat	240000000	8		20000	12.5
2 files, total time=25.0
differing intraExtra values: recording time 39.0

24. d18011
name	size	channels	samplingRate	minutes
d18011.002.dat	240000000	8		20000	12.5
d18011.003.dat	240000000	8		20000	12.5
d18011.004.dat	240000000	8		20000	12.5
d18011.005.dat	240000000	8		20000	12.5
d18011.001.dat	240000000	8		20000	12.5
5 files, total time=62.5
differing intraExtra values: recording time 120.0

25. d18021
name	size	channels	samplingRate	minutes
d18021.002.dat	240000000	8		20000	12.5
d18021.003.dat	240000000	8		20000	12.5
d18021.004.dat	240000000	8		20000	12.5
d18021.001.dat	240000000	8		20000	12.5
4 files, total time=50.0
differing intraExtra values: recording time 130.0

26. d18711
name	size	channels	samplingRate	minutes
d18711.002.dat	240000000	8		20000	12.5
d18711.003.dat	240000000	8		20000	12.5
d18711.001.dat	240000000	8		20000	12.5
3 files, total time=37.5
differing intraExtra values: recording time 54.0

27. d18712
name	size	channels	samplingRate	minutes
d18712.001.dat	240000000	8		20000	12.5
1 files, total time=12.5
differing intraExtra values: recording time 21.0

28. d18811
name	size	channels	samplingRate	minutes
d18811.001.dat	240000000	8		20000	12.5
1 files, total time=12.5
differing intraExtra values: recording time 55.0

29. d18911
name	size	channels	samplingRate	minutes
d18911.002.dat	240000000	8		20000	12.5
d18911.001.dat	240000000	8		20000	12.5
2 files, total time=25.0
differing intraExtra values: recording time 24.0, #_of_files '1/2'

30. d5331
name	size	channels	samplingRate	minutes
d533101.dat	38404096	8		10000	4.0
d533102.dat	38404096	8		10000	4.0
2 files, total time=8.0

31. d5611
name	size	channels	samplingRate	minutes
d561102.dat	38404096	8		10000	4.0
d561103.dat	38404096	8		10000	4.0
d561104.dat	38404096	8		10000	4.0
d561105.dat	38404096	8		10000	4.0
d561106.dat	76808192	8		20000	4.0
d561107.dat	76808192	8		20000	4.0
6 files, total time=24.0

32. d6111
name	size	channels	samplingRate	minutes
d611107.dat	76808192	8		20000	4.0
d611108.dat	76808192	8		20000	4.0
d611109.dat	76808192	8		20000	4.0
d611110.dat	76808192	8		20000	4.0
d611111.dat	76808192	8		20000	4.0
5 files, total time=20.0

33. d6811
name	size	channels	samplingRate	minutes
d681101.dat	38404096	8		10000	4.0
d681102.dat	38404096	8		10000	4.0
d681103.dat	38404096	8		10000	4.0
d681104.dat	38404096	8		10000	4.0
d681105.dat	38404096	8		10000	4.0
d681106.dat	38404096	8		10000	4.0
d681107.dat	38404096	8		10000	4.0
d681108.dat	38404096	8		10000	4.0
d681109.dat	38404096	8		10000	4.0
d681110.dat	38404096	8		10000	4.0
d681111.dat	38404096	8		10000	4.0
d681112.dat	38404096	8		10000	4.0
d681113.dat	38404096	8		10000	4.0
d681114.dat	38404096	8		10000	4.0
14 files, total time=56.01

34. d7111
name	size	channels	samplingRate	minutes
d711101.dat	38404096	8		10000	4.0
d711102.dat	38404096	8		10000	4.0
d711103.dat	38404096	8		10000	4.0
d711104.dat	38404096	8		10000	4.0
d711105.dat	38404096	8		10000	4.0
d711106.dat	38404096	8		10000	4.0
d711107.dat	38404096	8		10000	4.0
7 files, total time=28.0

35. d7211
name	size	channels	samplingRate	minutes
d721101.dat	38404096	8		10000	4.0
d721102.dat	38404096	8		10000	4.0
d721103.dat	38404096	8		10000	4.0
d721104.dat	38404096	8		10000	4.0
d721105.dat	38404096	8		10000	4.0
5 files, total time=20.0

36. d7212
name	size	channels	samplingRate	minutes
d721201.dat	38404096	8		10000	4.0
d721202.dat	38404096	8		10000	4.0
d721203.dat	38404096	8		10000	4.0
d721204.dat	38404096	8		10000	4.0
d721205.dat	38404096	8		10000	4.0
d721206.dat	38404096	8		10000	4.0
d721207.dat	38404096	8		10000	4.0
d721208.dat	38404096	8		10000	4.0
d721209.dat	38404096	8		10000	4.0
9 files, total time=36.0

37. d8131
name	size	channels	samplingRate	minutes
d081fre.001.dat	493000000	10		20000	20.54
d813101.dat	77070336	8		20000	4.01
d813102.dat	77070336	8		20000	4.01
3 files, total time=28.57, number of channels inconsistent

38. d8211
name	size	channels	samplingRate	minutes
d082free.001.dat		498880000	10	20000	20.79
d821101.dat			77070336	16	20000	2.01
d821102.dat			77070336	16	20000	2.01
3 files, total time=24.8, number of channels inconsistent

39. d8321
name	size	channels	samplingRate	minutes
d083dm.005.dat	240000000	10		20000	10.0
d083dm.006.dat	240000000	10		20000	10.0
d083dm.007.dat	240000000	10		20000	10.0
d083dm.008.dat	240000000	10		20000	10.0
d832101.dat	38404096	16		20000	1.0
d832102.dat	38404096	16		20000	1.0
6 files, total time=42.0, number of channels inconsistent

intraExtra.xls recording time difference (times are in minutes)
cell	       intraExtra     actual	 diff
d14521	       10.0	      12.5	 -2.5
d14921	       66.0	      32.5	 33.5
d15711	       60.0	      12.5	 47.5
d15712	       80.0	      37.5	 42.5
d16311	       120.0	      25.0	 95.0
d16613	       nan	      12.5	 nan
d17012	       10.0	      15.53	 -5.53
d17013	       60.0	      37.5	 22.5
d17014	       66.0	      12.5	 53.5
d17111	       46.0	      50.0	 -4.0
d17211	       36.0	      25.0	 11.0
d17212	       39.0	      25.0	 14.0
d18011	       120.0	      62.5	 57.5
d18021	       130.0	      50.0	 80.0
d18711	       54.0	      37.5	 16.5
d18712	       21.0	      12.5	 8.5
d18811	       55.0	      12.5	 42.5
d18911	       24.0	      25.0	 -1.0
39 cells, 18 in IntraExtra, 21 not in IntraExtra

```



  