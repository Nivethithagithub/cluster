import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data =
"1",1177.698,2,7,2,2,2,62000
"2",2134.8,5,7,4,2,2,78000
"3",1138.56,5,7,2,2,1,58000
"4",1458.78,2,7,3,2,2,45000
"5",967.776,11,14,3,2,2,45000
"6",1127.886,11,12,4,2,2,148000
"7",1352.04,5,7,3,2,1,58000
"8",757.854,5,14,1,0,1,48000
"9",1152.792,10,12,3,2,2,45000
"10",1423.2,4,5,4,2,2,65000
"11",668.904,4,11,1,1,1,31000
"12",711.6,4,7,2,1,1,29002
"13",1352.04,9,19,4,2,2,39000
"14",818.34,4,13,2,2,1,48000
"15",2134.8,10,19,3,2,2,55000
"16",2768.124,6,19,3,2,2,100000
"17",711.6,5,13,2,2,1,48000
"18",462.54,5,13,1,1,1,25000
"19",2739.66,6,19,3,2,2,90000
"20",1174.14,3,9,3,2,1,33000
"21",2490.6,19,21,5,3,4,140000
"22",2768.124,6,19,3,2,2,100000
"23",747.18,7,15,2,2,1,55000
"24",1668.702,4,12,3,2,2,105000
"25",3664.74,19,19,3,2,3,200000
"26",1779,10,12,4,2,2,98000
"27",3664.74,19,19,3,2,3,200000
"28",3059.88,21,24,4,2,3,145000
"29",533.7,3,4,1,1,1,25000
"30",853.92,6,7,2,1,1,24028
"31",1732.746,8,12,4,2,2,65000
"32",1245.3,10,12,3,0,0,85000
"33",2134.8,10,19,3,2,2,55000
"34",1206.162,7,7,2,2,1,57000
"35",861.036,5,12,2,2,1,46000
"36",462.54,3,4,1,1,1,52000
"37",434.076,5,12,2,2,1,43500
"38",768.528,4,4,3,2,2,60000
"39",3735.9,19,19,3,2,3,200000
"40",889.5,6,7,3,2,1,36000
"41",3063.438,21,24,5,2,4,145000
"42",925.08,10,14,2,1,1,48000
"43",1174.14,2,14,3,2,2,36000
"44",1352.04,1,4,4,2,2,65000
"45",1771.884,7,15,4,2,2,70000
"46",1601.1,6,7,4,2,2,50000
"47",1487.244,2,6,2,2,2,47999
"48",2277.12,2,25,3,2,2,80000
"49",3735.9,19,19,3,2,3,200000
"50",711.6,4,7,2,1,1,24030
"51",2241.54,7,13,4,2,2,76000
"52",1494.36,1,5,2,2,2,70000
"53",711.6,2,3,2,2,1,32500
"54",889.5,2,6,2,2,1,30032
"55",4643.19,1,6,5,4,4,180000
"56",2191.728,2,7,3,2,2,80000
"57",640.44,5,7,1,1,1,36000
"58",1067.4,12,12,3,2,2,36000
"59",640.44,2,6,2,2,1,29032
"60",1362.714,1,7,3,2,2,43000
"61",604.86,6,10,2,1,1,30000
"62",889.5,2,4,4,1,1,32000
"63",1423.2,5,7,3,2,2,45000
"64",1184.814,2,9,3,2,2,49000
"65",391.38,5,7,1,1,1,27500
"66",426.96,5,13,1,1,1,23000
"67",1067.4,4,5,3,2,1,33500
"68",533.7,2,7,2,1,1,26000
"69",462.54,6,14,1,1,1,27500
"70",1270.206,6,8,3,2,2,50000
"71",889.5,8,12,2,1,1,25000
"72",1284.438,6,12,3,2,2,41000
"73",1892.856,2,7,4,2,3,90000
"74",996.24,2,4,3,2,1,26000
"75",711.6,4,7,2,2,1,38000
"76",1754.094,3,7,3,2,2,75000
"77",2063.64,7,24,3,2,1,56000
"78",1522.824,5,12,4,2,2,40000
"79",1540.614,6,14,4,2,2,89900
"80",914.406,2,4,2,2,1,37000
"81",1558.404,5,7,4,2,2,48800
"82",772.086,6,7,2,1,1,39000
"83",711.6,8,9,2,2,1,45000
"84",747.18,5,9,2,2,2,50000
"85",1227.51,5,12,3,1,2,45000
"86",1451.664,2,5,3,3,2,46000
"87",3255.57,4,7,4,2,4,130000
"88",1779,7,12,4,2,2,60000
"89",1892.856,2,7,4,2,3,78000
"90",2312.7,7,15,4,2,2,70000
"91",1992.48,5,12,3,2,2,70000
"92",2063.64,5,7,4,2,2,70000
"93",1529.94,2,7,2,2,2,49800
"94",2145.474,5,6,4,2,2,79999
"95",2170.38,5,7,4,2,2,60000
"96",1771.884,4,7,4,2,2,57000
"97",1956.9,6,17,4,2,2,66000
"98",1743.42,3,7,4,2,2,75000
"99",1707.84,13,20,2,2,2,55000
"100",2063.64,5,7,4,2,2,70000
"102",2366.07,2,7,3,2,2,75000
"103",1814.58,2,16,3,2,2,60000
"104",2938.908,2,25,4,2,2,95000
"105",3173.736,3,9,3,2,3,150000
"106",2917.56,8,16,4,2,2,150000
"107",1786.116,3,6,4,2,3,98000
"108",3202.2,12,12,5,3,3,80000
"109",583.512,6,6,1,2,1,33000
"110",2099.22,7,15,4,2,2,55000
"111",2063.64,7,15,2,2,2,80000
"112",2099.22,7,15,4,2,2,52000
"113",857.478,6,9,4,2,2,52000
"114",2227.308,2,7,4,2,2,99999
"115",2088.546,8,19,3,2,2,65000
"116",1423.2,7,14,3,2,2,92000
"117",1569.078,6,7,3,2,2,55000
"118",3202.2,5,6,4,2,2,149999
"119",711.6,6,12,2,1,1,35000
"120",391.38,13,14,1,1,1,22000
"121",960.66,2,14,2,2,2,33000
"122",878.826,10,14,2,1,1,48000
"123",1280.88,10,12,3,2,2,53000
"124",2134.8,3,6,3,2,2,68000
"125",2149.032,5,6,4,2,2,80000
"126",2543.97,9,12,3,2,2,120000
"127",1206.162,7,7,2,2,1,57000
"128",1280.88,7,7,2,1,1,57000
"129",2067.198,4,14,4,2,2,100000
"130",1184.814,6,7,3,2,2,38000
"131",732.948,8,11,2,1,1,27000
"132",1529.94,6,12,3,2,2,75000
"133",1572.636,2,5,4,2,2,55000
"134",2540.412,18,18,4,2,2,89000
"135",1135.002,7,12,3,2,1,40000
"136",1544.172,5,16,3,2,2,99999
"137",1921.32,4,7,4,2,2,48000
"138",772.086,6,7,2,1,1,39000
"139",1754.094,3,7,3,2,2,75000
"140",2558.202,2,10,3,2,2,80000
"141",1195.488,10,16,3,2,2,86888
"142",3323.172,19,21,5,3,4,140000
"143",1223.952,6,7,4,2,2,58888
"144",1184.814,7,7,2,2,1,57000
"145",1223.952,3,7,3,2,2,41888
"146",1245.3,5,6,4,2,2,39000
"147",533.7,10,12,2,1,1,29999
"148",2028.06,6,15,4,2,2,88000
"149",4981.2,3,38,3,2,3,225000
"150",1245.3,6,7,3,2,2,40999
"151",1707.84,3,20,3,2,2,55000
"152",1779,10,13,4,2,2,97999
"153",1956.9,6,7,4,2,2,77000
"154",1779,2,7,4,2,2,57000
"155",889.5,10,14,2,1,1,52000
"156",996.24,11,14,3,2,2,44999
"158",1067.4,4,7,3,2,1,32000
"159",900.174,10,21,1,2,1,50000
"160",1704.282,3,6,3,2,2,59888
"161",1284.438,6,12,3,2,2,41000
"162",1565.52,2,6,3,2,1,45000
"163",1487.244,1,7,3,2,3,68000
"164",572.838,14,14,1,1,1,43000
"165",683.136,4,5,2,2,1,28000
"166",4091.7,2,15,3,2,4,180000
"167",1124.328,3,5,3,2,2,45000
"168",1789.674,10,12,4,2,2,88000
"169",1889.298,2,14,4,2,2,100000
"170",2205.96,4,15,3,2,2,100000
"171",1601.1,5,12,2,2,2,48000
"172",1085.19,12,19,2,2,1,35000
"173",1921.32,4,7,4,2,2,48000
"174",1707.84,9,15,3,2,2,80000
"175",2120.568,5,7,3,2,2,98000
"176",2782.356,12,13,3,2,3,120000
"177",914.406,2,4,2,2,1,37000
"178",1850.16,16,18,4,2,3,82000
"179",1889.298,2,14,4,2,2,100000
"180",1245.3,2,5,3,2,2,35000
"181",1494.36,2,7,2,2,2,49800
"182",1487.244,6,7,4,2,2,33700
"183",1690.05,7,14,3,2,2,40000
"184",796.992,3,12,2,2,2,45000
"185",3255.57,4,7,4,2,5,130000
"186",1063.842,3,7,2,1,1,45000
"187",1263.09,5,7,2,1,2,37000
"188",1352.04,5,5,3,2,2,36000
"189",1287.996,4,5,4,2,2,30000
"190",1167.024,3,12,3,2,2,42000
"191",1167.024,3,12,3,2,2,42000
"192",1839.486,2,13,1,0,1,67000
"193",796.992,3,12,2,2,1,45000
"194",601.302,2,9,1,1,1,38000
"195",2156.148,12,17,3,2,3,75000
"196",2138.358,11,14,4,2,2,55000
"197",1779,2,9,3,2,2,55000
"198",1779,8,15,3,2,2,85000
"199",1732.746,8,12,4,2,2,65000
"200",526.584,13,17,2,1,1,29500
"201",718.716,5,7,2,2,1,43000
"202",1601.1,3,7,3,2,2,33500
"203",1174.14,14,14,3,2,1,26000
"204",1408.968,9,9,2,2,2,65999
"205",1387.62,2,7,3,2,2,45000
"206",604.86,3,12,1,1,1,23800
"207",1380.504,6,13,3,2,2,49999
"208",2134.8,2,13,1,2,2,58000
"209",740.064,10,12,2,2,2,45000
"210",1031.82,5,12,2,2,2,36000
"211",1526.382,8,12,4,2,2,65000
"212",1601.1,1,4,3,2,2,65000
"213",1423.2,13,21,2,2,2,55000
"214",384.264,2,9,1,1,1,35000
"215",1996.038,5,12,3,2,2,75000
"216",718.716,5,7,2,2,1,43000
"217",1366.272,4,11,3,2,2,50000
"218",1743.42,3,12,3,2,2,45000
"219",1636.68,4,4,4,2,2,52000
"220",1903.53,8,13,3,2,2,120000
"221",668.904,5,6,2,1,1,28000
"222",2430.114,12,25,4,2,2,110000
"223",1298.67,7,7,2,2,1,57000
"224",2138.358,11,14,4,2,2,55000
"225",2963.814,2,25,4,2,2,95000
"226",533.7,14,16,1,1,1,25000
"227",2262.888,4,14,3,2,2,120000
"228",590.628,8,9,1,2,1,45000
"229",964.218,5,14,2,1,1,28000
"230",796.992,3,12,2,2,2,45000
"231",2408.766,6,13,4,2,3,80000
"232",1700.724,13,21,2,2,2,55000
"233",1672.26,3,7,3,2,2,75000
"234",1469.454,6,7,2,2,2,75000
"235",2067.198,4,14,4,2,2,100000
"236",1754.094,3,7,3,2,2,75000
"237",1757.652,4,16,4,2,2,55000
"238",587.07,5,7,1,1,1,36000
"239",1487.244,5,7,3,2,2,50000
"240",1487.244,5,7,3,2,2,50000
"241",789.876,7,9,1,1,1,42000
"242",2006.712,3,7,4,2,2,68000
"243",871.71,8,14,2,1,1,41999
"244",1522.824,11,11,4,2,3,60000
"245",3173.736,3,9,4,2,3,160000
"246",1899.972,21,27,4,2,2,57000
"247",2205.96,8,10,3,2,3,120000
"248",1106.538,3,12,1,2,1,50000
"249",2668.5,5,12,4,2,2,138888
"250",882.384,10,14,1,1,1,48800
"251",3255.57,4,7,4,2,5,120000
"252",2138.358,6,7,3,2,2,43000
"253",1579.752,4,15,3,1,2,99990
"254",2768.124,8,19,3,2,2,60000
"255",2081.43,10,17,2,2,2,68000
"256",1700.724,13,21,2,2,2,55000
"257",2134.8,6,7,3,2,2,43000
"258",718.716,5,12,2,1,1,34800
"259",754.296,5,7,2,1,1,80000
"260",1387.62,2,7,3,2,2,45000
"261",3558,1,5,2,2,2,63000
"262",1515.708,2,7,2,2,2,49800
"263",914.406,12,12,3,2,2,36000
"264",711.6,8,14,1,1,1,36000
"265",1487.244,2,6,2,2,2,48000
"266",2138.358,6,7,3,2,2,43000
"267",1127.886,4,5,3,2,2,26000
"268",1135.002,2,7,3,2,1,37000
"269",665.346,6,7,1,1,1,25000
"270",925.08,2,4,2,2,1,36000
"271",1209.72,3,4,3,2,2,38000
"272",1337.808,8,19,3,2,2,60000
"273",1366.272,4,11,4,2,2,49999
"274",2052.966,6,7,4,2,2,77999
"275",711.6,8,14,1,1,1,36000
"276",533.7,7,12,1,1,1,17000
"277",1138.56,4,5,3,2,2,26000
"278",1458.78,4,12,3,2,2,36000
"279",1245.3,5,7,2,2,2,37000
"280",1814.58,6,14,4,2,2,90000
"281",1515.708,4,7,2,2,2,88000
"282",811.224,5,12,2,1,1,43500
"283",359.358,12,12,1,1,1,26000
"284",1882.182,6,7,3,2,2,55000
"285",1419.642,6,12,4,2,2,50000
"286",1394.736,12,12,2,2,1,45000
"287",2063.64,3,6,4,2,3,88000
"288",1661.586,10,12,1,1,1,50000
"289",3504.63,13,14,2,2,2,250000
"291",1871.508,8,9,3,2,2,88000
"292",640.44,14,14,1,1,1,43000
"293",2430.114,5,25,3,2,2,88000
"294",1519.266,2,7,2,2,2,49800
"295",761.412,8,13,1,1,1,26000
"296",1903.53,8,13,2,2,2,120000
"297",1163.466,3,7,3,2,2,45000
"298",1779,4,4,4,2,2,51999
"299",1579.752,10,12,4,1,1,65000
"300",3145.272,2,25,4,2,2,98000
"301",3148.83,2,25,4,2,2,98000
"302",2700.522,15,21,5,2,4,100000
"303",3664.74,9,13,5,1,2,206000
"304",2134.8,2,6,3,2,2,68000
"305",1700.724,13,21,2,2,2,55000
"306",1380.504,6,13,3,2,2,49800
"307",2052.966,5,7,4,2,2,77999
"308",1871.508,11,12,4,2,2,49999
"309",1430.316,2,7,4,2,2,44999
"310",1579.752,4,15,3,1,2,99999
"311",1672.26,4,15,3,2,2,58000
"312",1270.206,3,14,2,2,1,42000
"313",1245.3,3,12,1,2,1,35000
"314",1458.78,4,6,2,1,2,65000
"315",1707.84,1,5,2,2,2,37000
"316",1515.708,2,7,2,2,2,48800
"317",1408.968,3,4,4,2,2,39999
"318",1476.57,6,6,3,2,2,49999
"319",1700.724,13,21,2,2,2,55000
"320",2590.224,7,7,4,3,3,77999
"321",2408.766,4,14,4,2,2,74999
"322",1779,10,10,3,2,2,90000
"323",2099.22,4,8,3,2,2,63000
"324",1206.162,7,7,2,2,1,59500
"325",989.124,13,13,2,2,1,45000
"326",3173.736,3,9,3,2,3,160000
"327",2444.346,7,15,4,2,3,73000
"328",722.274,11,13,2,1,1,36000
"329",1707.84,3,14,3,2,2,65000
"330",1444.548,6,7,2,2,1,53000
"331",2892.654,19,21,5,3,4,170000
"332",711.6,5,7,2,2,1,43000
"333",1423.2,13,21,2,2,2,55000
"334",1494.36,2,7,2,2,2,48800
"335",2184.612,2,9,3,2,2,80000
"336",601.302,2,9,1,1,1,35000
"337",3558,1,7,3,2,2,160000
"338",2102.778,6,12,3,2,2,70000
"339",1138.56,3,4,3,2,2,40000
"340",1579.752,3,12,5,1,1,56000
"341",1135.002,7,12,3,2,1,40000
"342",640.44,2,7,2,1,1,38000
"343",1515.708,2,6,3,2,2,68000
"344",747.18,9,12,2,2,1,60000
"345",754.296,5,14,2,2,1,32000
"346",2134.8,11,12,2,2,2,58000
"347",1490.802,3,12,2,1,2,59888
"348",1231.068,2,7,3,2,2,38888
"349",370.032,4,7,1,1,1,24888
"350",772.086,6,7,2,2,1,39000
"351",1622.448,1,6,3,2,2,130000
"352",925.08,2,4,2,1,1,31999
"353",818.34,5,9,1,2,1,42000
"354",1384.062,6,13,3,2,2,49800
"355",540.816,5,11,1,1,1,29500
"356",2561.76,10,17,4,2,3,100000
"357",1992.48,5,7,4,2,3,55000
"358",1031.82,11,14,3,2,2,61000
"359",2063.64,2,17,3,2,3,85000
"360",2312.7,7,16,5,2,3,55000
"361",2383.86,2,7,3,2,2,70000
"362",2134.8,5,7,4,2,2,78000
"363",2134.8,3,6,4,2,3,98000
"364",1423.2,3,12,3,2,2,50000
"365",1739.862,1,25,3,1,1,65000
"366",1191.93,3,7,3,2,2,55000
"367",711.6,6,14,1,1,1,39000
"368",658.23,4,4,1,1,1,22000
"369",537.258,22,26,1,0,1,19000
"370",1515.708,4,7,2,2,2,88000
"371",1732.746,8,12,4,2,2,65000
"372",640.44,8,9,1,2,1,45000
"373",925.08,2,4,2,1,1,31800
"374",718.716,5,12,2,2,1,34800
"375",426.96,9,12,1,0,1,13000
"376",658.23,9,12,2,2,1,46000
"377",1501.476,4,4,4,2,2,52000
"378",1771.884,4,7,4,2,2,57000
"379",1167.024,2,12,3,2,2,38000
"380",1252.416,8,12,3,2,2,40000
"381",1697.166,3,12,4,2,2,75000
"382",1167.024,2,12,3,2,2,43000
"383",2184.612,4,14,3,2,2,63000
"384",2170.38,9,15,4,2,2,110000
"385",1857.276,2,7,4,2,2,65000
"386",1996.038,5,12,3,2,2,70000
"387",1359.156,7,16,3,2,2,45000
"388",1586.868,3,7,3,2,2,44000
"389",2312.7,7,15,4,2,2,70000
"390",2227.308,2,5,5,2,2,100000
"391",893.058,8,14,2,2,1,38000
"392",1440.99,6,7,2,2,1,55000
"393",1263.09,5,7,2,2,2,37000
"394",1099.422,2,7,4,2,2,58500
"395",3255.57,4,7,4,2,5,120000
"396",1540.614,6,14,4,2,2,69000
"397",1366.272,10,12,3,2,2,41000
"398",1152.792,10,12,2,2,2,45000
"399",1544.172,10,12,4,2,2,98000
"400",1910.646,6,7,4,2,2,75000
"401",718.716,5,12,2,2,1,35000
"402",1487.244,6,7,3,2,2,33700
"403",1312.902,4,13,3,2,2,41000
"404",1255.974,4,16,3,2,2,40000
"405",2255.772,2,25,3,2,2,80000
"406",2052.966,5,7,4,2,2,78000
"407",1188.372,2,14,3,2,2,36000
"408",604.86,5,5,2,0,1,11900
"409",889.5,3,4,2,2,1,29800
"410",1067.4,1,6,3,2,2,35000
"411",1138.56,6,10,2,1,2,33000
"412",925.08,4,13,2,2,1,32000
"413",711.6,6,9,2,2,1,42000
"414",925.08,2,4,3,1,1,34500
"415",925.08,4,13,2,2,1,32000
"416",523.026,2,12,1,1,1,29000
"417",1529.94,2,12,2,2,1,58000
"418",836.13,8,12,2,1,1,35000
"419",789.876,7,9,1,1,1,42000
"420",1885.74,6,7,3,2,2,54999
"421",2782.356,12,13,3,2,3,123456
"422",711.6,5,7,3,2,2,28000
"423",469.656,7,7,1,1,1,34000
"424",793.434,11,14,2,1,1,40000
"425",1565.52,2,6,3,2,1,45000
"426",1366.272,4,11,4,2,2,50000
"427",1914.204,17,21,3,2,2,88000
"428",1889.298,2,14,4,2,2,100000
"429",1956.9,6,7,4,2,3,85000
"430",1992.48,4,15,3,2,2,99888
"431",3187.968,6,7,3,2,2,168000
"432",925.08,2,18,1,2,1,51000
"433",1067.4,4,7,3,2,2,31000
"434",1352.04,17,24,3,2,2,85000
"435",2063.64,15,15,3,2,2,110000
"436",796.992,3,12,2,2,2,45000
"437",949.986,5,12,2,1,1,43000
"438",2910.444,4,7,3,2,3,90000
"439",3010.068,4,11,3,2,2,185000
"440",768.528,6,7,1,1,1,45000
"441",772.086,3,7,2,2,1,28000
"442",1423.2,3,7,3,2,2,68000
"443",1380.504,2,12,3,2,2,42000
"444",448.308,2,12,1,1,1,17000
"445",1971.132,2,6,4,2,2,53000
"446",2052.966,5,7,4,2,2,78000
"447",1127.886,11,12,3,2,2,150000
"448",3241.338,7,7,2,2,3,99999
"449",1892.856,9,12,3,2,2,119999
"450",2138.358,4,7,4,2,3,100000
"451",1423.2,2,7,4,1,2,45000
"452",1754.094,3,7,4,2,2,48000
"453",925.08,2,4,2,2,1,36000
"454",1352.04,4,11,4,2,2,50000
"455",889.5,5,5,2,1,1,24000
"456",640.44,2,5,1,1,1,28000
"457",1423.2,3,4,4,2,2,39000
"458",651.114,8,11,3,2,2,36000
"459",1391.178,1,7,1,3,3,50000
"460",1487.244,6,7,3,2,2,36000
"461",1700.724,13,21,2,2,2,55000
"462",1515.708,6,7,4,2,2,50000
"463",1206.162,7,7,2,2,1,57000
"464",2052.966,5,7,4,2,2,78000
"465",1298.67,7,7,2,2,1,59500
"466",1444.548,2,5,4,2,2,45000
"467",2067.198,4,14,4,2,2,100000
"468",1227.51,2,7,3,2,2,39000
"469",1494.36,4,4,3,2,2,36000
"470",1366.272,4,11,4,2,2,50000
"471",2298.468,14,18,4,2,2,135000
"472",925.08,7,10,1,2,1,28000
"473",3842.64,15,16,3,1,2,200000
"474",1889.298,2,14,4,2,2,105000
"475",2063.64,3,6,4,2,2,98000
"476",1544.172,10,12,4,2,2,98000
"477",1273.764,5,13,3,2,2,57000
"478",1579.752,4,15,3,2,2,100000
"479",1672.26,10,12,2,1,2,45000
"480",1227.51,5,12,2,2,2,45000
"481",1401.852,2,6,3,2,3,60000
"482",569.28,9,9,2,2,1,32000
"483",2173.938,5,7,4,2,2,60000
"484",2213.076,2,14,4,2,2,108000
"485",2063.64,4,14,4,2,2,100000
"486",1707.84,9,15,3,2,2,80000
"487",900.174,4,7,2,2,2,88000
"488",1465.896,6,7,2,2,2,80000
"489",1316.46,4,13,3,2,2,45000
"490",740.064,6,14,1,1,1,38800
"491",754.296,2,9,1,1,1,35000
"492",1647.354,10,14,2,2,2,55000
"493",811.224,5,12,2,1,1,43500
"494",1487.244,8,12,4,2,2,38000
"495",1494.36,1,4,4,2,3,150000
"496",2914.002,5,15,3,2,2,110000
"497",1665.144,7,12,4,2,2,48000
"498",1732.746,8,12,4,2,2,72000
"499",853.92,8,14,2,1,1,42000
"500",1885.74,6,7,4,2,2,75000
"501",889.5,11,13,2,2,2,49998
"502",2455.02,12,25,4,2,2,110000
"503",1067.4,6,9,4,2,2,50000
"504",1102.98,2,9,3,2,2,50000
"505",3024.3,9,13,3,2,2,158000
"506",1102.98,2,4,3,1,2,26000
"507",1725.63,4,12,3,2,2,45000
"508",985.566,8,14,2,2,1,28000
"509",1102.98,3,7,3,2,2,35000
"510",1885.74,7,12,3,1,2,77000
"511",2028.06,12,12,5,1,1,89000
"512",540.816,5,11,2,1,1,28500
"513",590.628,8,9,2,1,1,45000
"514",2170.38,9,15,4,2,2,110000
"515",1992.48,5,12,3,2,2,70000
"516",960.66,4,5,3,2,2,33000
"517",843.246,2,18,1,1,1,51500
"518",1889.298,18,21,3,2,2,69500
"519",1487.244,6,7,3,1,2,36000
"520",587.07,5,7,1,1,1,36000
"521",1384.062,6,13,3,2,2,50000
"522",818.34,4,5,3,2,1,21000
"523",711.6,1,4,2,2,3,42000
"524",1074.516,7,10,3,1,2,35000
"525",391.38,7,14,1,2,1,25000
"526",1889.298,2,14,4,2,2,100000
"527",1031.82,4,16,3,2,2,40000
"528",1921.32,3,7,4,2,2,55000
"529",1387.62,4,4,3,2,2,40000
"530",1352.04,9,14,3,2,2,50000
"531",1433.874,5,6,3,2,2,47000
"532",462.54,13,14,1,1,1,20000
"533",3775.038,11,11,3,3,3,150000
"534",996.24,2,5,3,2,1,28000
"535",441.192,3,6,1,2,1,40000
"536",1757.652,6,7,4,2,3,65000
"537",1974.69,6,17,4,2,2,70000
"538",711.6,5,7,2,2,1,43000
"539",1825.254,5,7,3,2,2,60000
"540",1814.58,6,14,4,2,3,85000
"541",1426.758,3,12,3,2,2,48120
"542",469.656,9,12,1,1,1,35000
"543",1149.234,10,12,3,2,1,50000
"544",2309.142,16,21,4,2,4,138000
"545",1102.98,2,4,2,1,2,31000
"546",782.76,3,5,2,1,1,30000
"547",1352.04,9,13,3,2,2,48000
"548",1494.36,6,7,4,1,2,60000
"549",1245.3,5,6,3,2,2,40000
"550",1529.94,2,7,4,2,2,45000
"551",1569.078,10,12,2,2,2,58000
"552",1352.04,2,4,4,2,2,30000
"553",2141.916,7,19,4,2,2,77000
"554",1565.52,1,5,3,2,3,80000
"555",1885.74,2,7,4,2,2,55000
"556",1761.21,3,6,3,2,2,45000
"557",1761.21,3,6,4,2,2,45000
"558",889.5,11,18,2,2,1,30500
"559",2668.5,5,12,4,2,2,138888
"560",1334.25,5,11,3,2,2,38000
"561",925.08,1,4,2,2,1,36000
"562",878.826,10,14,1,1,1,47999
"563",1067.4,3,12,3,2,1,35000
"564",1423.2,11,12,2,2,2,38000
"565",1419.642,3,7,3,2,2,45000
"566",711.6,5,5,2,2,1,22000
"567",718.716,5,12,2,2,1,35000
"568",1956.9,9,12,4,2,2,90000
"569",1544.172,10,12,4,2,2,98000
"570",2383.86,1,7,5,3,3,60000
"571",2081.43,10,17,3,2,2,68000
"572",711.6,6,6,2,1,1,17000
"573",700.926,7,11,2,1,1,40000
"574",1181.256,1,4,3,2,2,52000
"575",498.12,11,14,2,1,1,40000
"576",5856.468,7,21,6,2,5,180000
"577",1245.3,8,8,3,2,2,23000
"578",868.152,3,5,3,2,1,26000
"579",533.7,7,7,1,1,1,28800
"580",693.81,2,7,1,1,1,33000
"581",1576.194,3,7,4,2,2,44000
"582",5760.402,9,15,3,2,3,170000
"583",796.992,3,12,2,2,1,45000
"584",2052.966,5,7,4,2,2,78000
"585",1163.466,2,7,3,2,2,38000
"586",1316.46,4,15,3,2,2,45000
"587",1099.422,4,12,2,2,1,38800
"588",1480.128,4,7,2,2,2,99999
"589",2739.66,5,21,4,2,2,150000
"590",800.55,3,4,2,2,1,43000
"591",676.02,6,7,2,1,1,45000
"592",964.218,4,4,3,2,1,32000
"593",1832.37,9,16,4,2,2,69000
"594",782.76,10,14,1,0,1,31000
"595",1551.288,5,5,4,2,2,59800
"596",1102.98,2,4,2,2,2,31000
"597",989.124,9,12,3,2,2,42000
"598",711.6,9,14,2,1,1,27000
"599",1458.78,6,7,3,2,2,36000
"600",1359.156,7,16,3,2,2,45000
"601",2063.64,5,9,4,2,2,60000
"602",846.804,14,14,2,2,1,29000
"603",1458.78,21,27,3,2,2,60000
"604",1127.886,4,5,3,2,2,26000
"605",1355.598,5,19,2,2,2,69999
"606",1892.856,5,12,4,2,2,129999
"607",1031.82,3,6,3,2,2,21000
"608",1707.84,5,7,3,2,2,50000
"609",640.44,9,12,2,1,1,45000
"610",1014.03,8,11,3,2,2,36000
"611",1067.4,6,14,3,2,1,43000
"612",711.6,8,12,1,2,1,30000
"613",996.24,4,5,3,2,1,6100
"614",2134.8,3,6,4,2,3,98000
"615",1647.354,11,14,4,2,2,55000
"616",1138.56,3,12,3,2,2,42000
"617",889.5,5,9,1,1,1,43000
"618",711.6,8,14,1,1,1,36000
"619",1857.276,2,14,3,2,2,45000
"620",1102.98,6,7,3,2,2,65000
"621",925.08,2,4,2,1,1,32000
"622",2312.7,11,14,3,2,2,99999
"623",925.08,4,9,3,2,2,45000
"624",711.6,1,1,3,1,1,12000
"625",4198.44,15,19,7,3,4,180000
"626",3095.46,1,6,4,2,3,100000
"627",2590.224,5,15,3,2,3,110000
"628",1885.74,8,13,3,2,2,120000
"629",1245.3,1,14,3,2,2,55000
"630",1174.14,10,12,3,2,2,41000
"631",1458.78,6,7,2,2,2,75000
"632",1305.786,9,12,3,2,2,42000
"633",1316.46,12,12,3,2,2,45000
"634",1167.024,2,12,3,2,2,38000
"635",996.24,3,5,3,1,1,28000
"636",1099.422,2,7,4,2,2,57777
"637",2042.292,6,18,2,2,2,82000
"638",843.246,2,18,1,1,1,53000
"639",1889.298,18,21,3,2,2,70000
"640",1266.648,6,7,3,2,2,40000
"641",1707.84,9,9,4,2,2,60000
"642",1707.84,9,15,3,2,2,80000
"643",2846.4,5,12,4,2,2,138888
"644",1359.156,7,15,3,2,2,45000
"645",377.148,4,10,1,1,1,24800
"646",740.064,13,14,1,1,1,45000
"647",1707.84,3,14,3,2,2,65000
"648",1376.946,6,7,3,2,1,36000
df = pd.read_csv(pd.compat.StringIO(data), header=None)
df = df.drop(columns=[0])
X = df.to_numpy()
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method to Find Optimal k')
plt.show()
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X)
df['Cluster'] = kmeans.labels_
print(df)
