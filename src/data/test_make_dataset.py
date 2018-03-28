import unittest
import csv
from io import StringIO

from .make_dataset import construct_line


class TestMakeDataset(unittest.TestCase):

    def test_construct_line(self):
        scsv = "ip,app,device,os,channel,click_time,attributed_time,is_attributed\n87540,12,1,13,497,2017-11-07 09:30:38,,0"
        f = StringIO(scsv)
        for row in csv.DictReader(f):
            self.assertEqual("-1 |ip 87540 |app 12 |device 1 |os 13 |channel 497\n", construct_line(row))

    def test_construct_line_zero(self):
        scsv = "ip,app,device,os,channel,click_time,is_attributed,PERCENT_TRUE(clicks.is_attributed),MINUTE(first_clicks_time),MEAN(clicks.time_since_previous_by_app)\n181628,12,1,17,245,2017-11-07 04:00:00,0,0.00014440579548592551,0.0,0.0"
        f = StringIO(scsv)
        for row in csv.DictReader(f):
            print(construct_line(row))

    def test_construct_line_features(self):
        scsv = "ip,app,device,os,channel,click_time,is_attributed,SUM(clicks.is_attributed),STD(clicks.is_attributed),MAX(clicks.is_attributed),SKEW(clicks.is_attributed),MIN(clicks.is_attributed),MEAN(clicks.is_attributed),COUNT(clicks),NUM_UNIQUE(clicks.ip),NUM_UNIQUE(clicks.device),NUM_UNIQUE(clicks.os),NUM_UNIQUE(clicks.channel),MODE(clicks.ip),MODE(clicks.device),MODE(clicks.os),MODE(clicks.channel),DAY(first_clicks_time),YEAR(first_clicks_time),MONTH(first_clicks_time),WEEKDAY(first_clicks_time),NUM_UNIQUE(clicks.DAY(click_time)),NUM_UNIQUE(clicks.YEAR(click_time)),NUM_UNIQUE(clicks.MONTH(click_time)),NUM_UNIQUE(clicks.WEEKDAY(click_time)),MODE(clicks.DAY(click_time)),MODE(clicks.YEAR(click_time)),MODE(clicks.MONTH(click_time)),MODE(clicks.WEEKDAY(click_time)),SUM(clicks.ips.SUM(clicks.is_attributed)),SUM(clicks.ips.STD(clicks.is_attributed)),SUM(clicks.ips.MAX(clicks.is_attributed)),SUM(clicks.ips.SKEW(clicks.is_attributed)),SUM(clicks.ips.MIN(clicks.is_attributed)),SUM(clicks.ips.MEAN(clicks.is_attributed)),SUM(clicks.ips.COUNT(clicks)),SUM(clicks.ips.NUM_UNIQUE(clicks.app)),SUM(clicks.ips.NUM_UNIQUE(clicks.device)),SUM(clicks.ips.NUM_UNIQUE(clicks.os)),SUM(clicks.ips.NUM_UNIQUE(clicks.channel)),SUM(clicks.devices.SUM(clicks.is_attributed)),SUM(clicks.devices.STD(clicks.is_attributed)),SUM(clicks.devices.MAX(clicks.is_attributed)),SUM(clicks.devices.SKEW(clicks.is_attributed)),SUM(clicks.devices.MIN(clicks.is_attributed)),SUM(clicks.devices.MEAN(clicks.is_attributed)),SUM(clicks.devices.COUNT(clicks)),SUM(clicks.devices.NUM_UNIQUE(clicks.ip)),SUM(clicks.devices.NUM_UNIQUE(clicks.app)),SUM(clicks.devices.NUM_UNIQUE(clicks.os)),SUM(clicks.devices.NUM_UNIQUE(clicks.channel)),SUM(clicks.oses.SUM(clicks.is_attributed)),SUM(clicks.oses.STD(clicks.is_attributed)),SUM(clicks.oses.MAX(clicks.is_attributed)),SUM(clicks.oses.SKEW(clicks.is_attributed)),SUM(clicks.oses.MIN(clicks.is_attributed)),SUM(clicks.oses.MEAN(clicks.is_attributed)),SUM(clicks.oses.COUNT(clicks)),SUM(clicks.oses.NUM_UNIQUE(clicks.ip)),SUM(clicks.oses.NUM_UNIQUE(clicks.app)),SUM(clicks.oses.NUM_UNIQUE(clicks.device)),SUM(clicks.oses.NUM_UNIQUE(clicks.channel)),SUM(clicks.channels.SUM(clicks.is_attributed)),SUM(clicks.channels.STD(clicks.is_attributed)),SUM(clicks.channels.MAX(clicks.is_attributed)),SUM(clicks.channels.SKEW(clicks.is_attributed)),SUM(clicks.channels.MIN(clicks.is_attributed)),SUM(clicks.channels.MEAN(clicks.is_attributed)),SUM(clicks.channels.COUNT(clicks)),SUM(clicks.channels.NUM_UNIQUE(clicks.ip)),SUM(clicks.channels.NUM_UNIQUE(clicks.app)),SUM(clicks.channels.NUM_UNIQUE(clicks.device)),SUM(clicks.channels.NUM_UNIQUE(clicks.os)),STD(clicks.ips.SUM(clicks.is_attributed)),STD(clicks.ips.STD(clicks.is_attributed)),STD(clicks.ips.MAX(clicks.is_attributed)),STD(clicks.ips.SKEW(clicks.is_attributed)),STD(clicks.ips.MIN(clicks.is_attributed)),STD(clicks.ips.MEAN(clicks.is_attributed)),STD(clicks.ips.COUNT(clicks)),STD(clicks.ips.NUM_UNIQUE(clicks.app)),STD(clicks.ips.NUM_UNIQUE(clicks.device)),STD(clicks.ips.NUM_UNIQUE(clicks.os)),STD(clicks.ips.NUM_UNIQUE(clicks.channel)),STD(clicks.devices.SUM(clicks.is_attributed)),STD(clicks.devices.STD(clicks.is_attributed)),STD(clicks.devices.MAX(clicks.is_attributed)),STD(clicks.devices.SKEW(clicks.is_attributed)),STD(clicks.devices.MIN(clicks.is_attributed)),STD(clicks.devices.MEAN(clicks.is_attributed)),STD(clicks.devices.COUNT(clicks)),STD(clicks.devices.NUM_UNIQUE(clicks.ip)),STD(clicks.devices.NUM_UNIQUE(clicks.app)),STD(clicks.devices.NUM_UNIQUE(clicks.os)),STD(clicks.devices.NUM_UNIQUE(clicks.channel)),STD(clicks.oses.SUM(clicks.is_attributed)),STD(clicks.oses.STD(clicks.is_attributed)),STD(clicks.oses.MAX(clicks.is_attributed)),STD(clicks.oses.SKEW(clicks.is_attributed)),STD(clicks.oses.MIN(clicks.is_attributed)),STD(clicks.oses.MEAN(clicks.is_attributed)),STD(clicks.oses.COUNT(clicks)),STD(clicks.oses.NUM_UNIQUE(clicks.ip)),STD(clicks.oses.NUM_UNIQUE(clicks.app)),STD(clicks.oses.NUM_UNIQUE(clicks.device)),STD(clicks.oses.NUM_UNIQUE(clicks.channel)),STD(clicks.channels.SUM(clicks.is_attributed)),STD(clicks.channels.STD(clicks.is_attributed)),STD(clicks.channels.MAX(clicks.is_attributed)),STD(clicks.channels.SKEW(clicks.is_attributed)),STD(clicks.channels.MIN(clicks.is_attributed)),STD(clicks.channels.MEAN(clicks.is_attributed)),STD(clicks.channels.COUNT(clicks)),STD(clicks.channels.NUM_UNIQUE(clicks.ip)),STD(clicks.channels.NUM_UNIQUE(clicks.app)),STD(clicks.channels.NUM_UNIQUE(clicks.device)),STD(clicks.channels.NUM_UNIQUE(clicks.os)),MAX(clicks.ips.SUM(clicks.is_attributed)),MAX(clicks.ips.STD(clicks.is_attributed)),MAX(clicks.ips.MAX(clicks.is_attributed)),MAX(clicks.ips.SKEW(clicks.is_attributed)),MAX(clicks.ips.MIN(clicks.is_attributed)),MAX(clicks.ips.MEAN(clicks.is_attributed)),MAX(clicks.ips.COUNT(clicks)),MAX(clicks.ips.NUM_UNIQUE(clicks.app)),MAX(clicks.ips.NUM_UNIQUE(clicks.device)),MAX(clicks.ips.NUM_UNIQUE(clicks.os)),MAX(clicks.ips.NUM_UNIQUE(clicks.channel)),MAX(clicks.devices.SUM(clicks.is_attributed)),MAX(clicks.devices.STD(clicks.is_attributed)),MAX(clicks.devices.MAX(clicks.is_attributed)),MAX(clicks.devices.SKEW(clicks.is_attributed)),MAX(clicks.devices.MIN(clicks.is_attributed)),MAX(clicks.devices.MEAN(clicks.is_attributed)),MAX(clicks.devices.COUNT(clicks)),MAX(clicks.devices.NUM_UNIQUE(clicks.ip)),MAX(clicks.devices.NUM_UNIQUE(clicks.app)),MAX(clicks.devices.NUM_UNIQUE(clicks.os)),MAX(clicks.devices.NUM_UNIQUE(clicks.channel)),MAX(clicks.oses.SUM(clicks.is_attributed)),MAX(clicks.oses.STD(clicks.is_attributed)),MAX(clicks.oses.MAX(clicks.is_attributed)),MAX(clicks.oses.SKEW(clicks.is_attributed)),MAX(clicks.oses.MIN(clicks.is_attributed)),MAX(clicks.oses.MEAN(clicks.is_attributed)),MAX(clicks.oses.COUNT(clicks)),MAX(clicks.oses.NUM_UNIQUE(clicks.ip)),MAX(clicks.oses.NUM_UNIQUE(clicks.app)),MAX(clicks.oses.NUM_UNIQUE(clicks.device)),MAX(clicks.oses.NUM_UNIQUE(clicks.channel)),MAX(clicks.channels.SUM(clicks.is_attributed)),MAX(clicks.channels.STD(clicks.is_attributed)),MAX(clicks.channels.MAX(clicks.is_attributed)),MAX(clicks.channels.SKEW(clicks.is_attributed)),MAX(clicks.channels.MIN(clicks.is_attributed)),MAX(clicks.channels.MEAN(clicks.is_attributed)),MAX(clicks.channels.COUNT(clicks)),MAX(clicks.channels.NUM_UNIQUE(clicks.ip)),MAX(clicks.channels.NUM_UNIQUE(clicks.app)),MAX(clicks.channels.NUM_UNIQUE(clicks.device)),MAX(clicks.channels.NUM_UNIQUE(clicks.os)),SKEW(clicks.ips.SUM(clicks.is_attributed)),SKEW(clicks.ips.STD(clicks.is_attributed)),SKEW(clicks.ips.MAX(clicks.is_attributed)),SKEW(clicks.ips.SKEW(clicks.is_attributed)),SKEW(clicks.ips.MIN(clicks.is_attributed)),SKEW(clicks.ips.MEAN(clicks.is_attributed)),SKEW(clicks.ips.COUNT(clicks)),SKEW(clicks.ips.NUM_UNIQUE(clicks.app)),SKEW(clicks.ips.NUM_UNIQUE(clicks.device)),SKEW(clicks.ips.NUM_UNIQUE(clicks.os)),SKEW(clicks.ips.NUM_UNIQUE(clicks.channel)),SKEW(clicks.devices.SUM(clicks.is_attributed)),SKEW(clicks.devices.STD(clicks.is_attributed)),SKEW(clicks.devices.MAX(clicks.is_attributed)),SKEW(clicks.devices.SKEW(clicks.is_attributed)),SKEW(clicks.devices.MIN(clicks.is_attributed)),SKEW(clicks.devices.MEAN(clicks.is_attributed)),SKEW(clicks.devices.COUNT(clicks)),SKEW(clicks.devices.NUM_UNIQUE(clicks.ip)),SKEW(clicks.devices.NUM_UNIQUE(clicks.app)),SKEW(clicks.devices.NUM_UNIQUE(clicks.os)),SKEW(clicks.devices.NUM_UNIQUE(clicks.channel)),SKEW(clicks.oses.SUM(clicks.is_attributed)),SKEW(clicks.oses.STD(clicks.is_attributed)),SKEW(clicks.oses.MAX(clicks.is_attributed)),SKEW(clicks.oses.SKEW(clicks.is_attributed)),SKEW(clicks.oses.MIN(clicks.is_attributed)),SKEW(clicks.oses.MEAN(clicks.is_attributed)),SKEW(clicks.oses.COUNT(clicks)),SKEW(clicks.oses.NUM_UNIQUE(clicks.ip)),SKEW(clicks.oses.NUM_UNIQUE(clicks.app)),SKEW(clicks.oses.NUM_UNIQUE(clicks.device)),SKEW(clicks.oses.NUM_UNIQUE(clicks.channel)),SKEW(clicks.channels.SUM(clicks.is_attributed)),SKEW(clicks.channels.STD(clicks.is_attributed)),SKEW(clicks.channels.MAX(clicks.is_attributed)),SKEW(clicks.channels.SKEW(clicks.is_attributed)),SKEW(clicks.channels.MIN(clicks.is_attributed)),SKEW(clicks.channels.MEAN(clicks.is_attributed)),SKEW(clicks.channels.COUNT(clicks)),SKEW(clicks.channels.NUM_UNIQUE(clicks.ip)),SKEW(clicks.channels.NUM_UNIQUE(clicks.app)),SKEW(clicks.channels.NUM_UNIQUE(clicks.device)),SKEW(clicks.channels.NUM_UNIQUE(clicks.os)),MIN(clicks.ips.SUM(clicks.is_attributed)),MIN(clicks.ips.STD(clicks.is_attributed)),MIN(clicks.ips.MAX(clicks.is_attributed)),MIN(clicks.ips.SKEW(clicks.is_attributed)),MIN(clicks.ips.MIN(clicks.is_attributed)),MIN(clicks.ips.MEAN(clicks.is_attributed)),MIN(clicks.ips.COUNT(clicks)),MIN(clicks.ips.NUM_UNIQUE(clicks.app)),MIN(clicks.ips.NUM_UNIQUE(clicks.device)),MIN(clicks.ips.NUM_UNIQUE(clicks.os)),MIN(clicks.ips.NUM_UNIQUE(clicks.channel)),MIN(clicks.devices.SUM(clicks.is_attributed)),MIN(clicks.devices.STD(clicks.is_attributed)),MIN(clicks.devices.MAX(clicks.is_attributed)),MIN(clicks.devices.SKEW(clicks.is_attributed)),MIN(clicks.devices.MIN(clicks.is_attributed)),MIN(clicks.devices.MEAN(clicks.is_attributed)),MIN(clicks.devices.COUNT(clicks)),MIN(clicks.devices.NUM_UNIQUE(clicks.ip)),MIN(clicks.devices.NUM_UNIQUE(clicks.app)),MIN(clicks.devices.NUM_UNIQUE(clicks.os)),MIN(clicks.devices.NUM_UNIQUE(clicks.channel)),MIN(clicks.oses.SUM(clicks.is_attributed)),MIN(clicks.oses.STD(clicks.is_attributed)),MIN(clicks.oses.MAX(clicks.is_attributed)),MIN(clicks.oses.SKEW(clicks.is_attributed)),MIN(clicks.oses.MIN(clicks.is_attributed)),MIN(clicks.oses.MEAN(clicks.is_attributed)),MIN(clicks.oses.COUNT(clicks)),MIN(clicks.oses.NUM_UNIQUE(clicks.ip)),MIN(clicks.oses.NUM_UNIQUE(clicks.app)),MIN(clicks.oses.NUM_UNIQUE(clicks.device)),MIN(clicks.oses.NUM_UNIQUE(clicks.channel)),MIN(clicks.channels.SUM(clicks.is_attributed)),MIN(clicks.channels.STD(clicks.is_attributed)),MIN(clicks.channels.MAX(clicks.is_attributed)),MIN(clicks.channels.SKEW(clicks.is_attributed)),MIN(clicks.channels.MIN(clicks.is_attributed)),MIN(clicks.channels.MEAN(clicks.is_attributed)),MIN(clicks.channels.COUNT(clicks)),MIN(clicks.channels.NUM_UNIQUE(clicks.ip)),MIN(clicks.channels.NUM_UNIQUE(clicks.app)),MIN(clicks.channels.NUM_UNIQUE(clicks.device)),MIN(clicks.channels.NUM_UNIQUE(clicks.os)),MEAN(clicks.ips.SUM(clicks.is_attributed)),MEAN(clicks.ips.STD(clicks.is_attributed)),MEAN(clicks.ips.MAX(clicks.is_attributed)),MEAN(clicks.ips.SKEW(clicks.is_attributed)),MEAN(clicks.ips.MIN(clicks.is_attributed)),MEAN(clicks.ips.MEAN(clicks.is_attributed)),MEAN(clicks.ips.COUNT(clicks)),MEAN(clicks.ips.NUM_UNIQUE(clicks.app)),MEAN(clicks.ips.NUM_UNIQUE(clicks.device)),MEAN(clicks.ips.NUM_UNIQUE(clicks.os)),MEAN(clicks.ips.NUM_UNIQUE(clicks.channel)),MEAN(clicks.devices.SUM(clicks.is_attributed)),MEAN(clicks.devices.STD(clicks.is_attributed)),MEAN(clicks.devices.MAX(clicks.is_attributed)),MEAN(clicks.devices.SKEW(clicks.is_attributed)),MEAN(clicks.devices.MIN(clicks.is_attributed)),MEAN(clicks.devices.MEAN(clicks.is_attributed)),MEAN(clicks.devices.COUNT(clicks)),MEAN(clicks.devices.NUM_UNIQUE(clicks.ip)),MEAN(clicks.devices.NUM_UNIQUE(clicks.app)),MEAN(clicks.devices.NUM_UNIQUE(clicks.os)),MEAN(clicks.devices.NUM_UNIQUE(clicks.channel)),MEAN(clicks.oses.SUM(clicks.is_attributed)),MEAN(clicks.oses.STD(clicks.is_attributed)),MEAN(clicks.oses.MAX(clicks.is_attributed)),MEAN(clicks.oses.SKEW(clicks.is_attributed)),MEAN(clicks.oses.MIN(clicks.is_attributed)),MEAN(clicks.oses.MEAN(clicks.is_attributed)),MEAN(clicks.oses.COUNT(clicks)),MEAN(clicks.oses.NUM_UNIQUE(clicks.ip)),MEAN(clicks.oses.NUM_UNIQUE(clicks.app)),MEAN(clicks.oses.NUM_UNIQUE(clicks.device)),MEAN(clicks.oses.NUM_UNIQUE(clicks.channel)),MEAN(clicks.channels.SUM(clicks.is_attributed)),MEAN(clicks.channels.STD(clicks.is_attributed)),MEAN(clicks.channels.MAX(clicks.is_attributed)),MEAN(clicks.channels.SKEW(clicks.is_attributed)),MEAN(clicks.channels.MIN(clicks.is_attributed)),MEAN(clicks.channels.MEAN(clicks.is_attributed)),MEAN(clicks.channels.COUNT(clicks)),MEAN(clicks.channels.NUM_UNIQUE(clicks.ip)),MEAN(clicks.channels.NUM_UNIQUE(clicks.app)),MEAN(clicks.channels.NUM_UNIQUE(clicks.device)),MEAN(clicks.channels.NUM_UNIQUE(clicks.os)),NUM_UNIQUE(clicks.ips.MODE(clicks.app)),NUM_UNIQUE(clicks.ips.MODE(clicks.device)),NUM_UNIQUE(clicks.ips.MODE(clicks.os)),NUM_UNIQUE(clicks.ips.MODE(clicks.channel)),NUM_UNIQUE(clicks.ips.DAY(first_clicks_time)),NUM_UNIQUE(clicks.ips.YEAR(first_clicks_time)),NUM_UNIQUE(clicks.ips.MONTH(first_clicks_time)),NUM_UNIQUE(clicks.ips.WEEKDAY(first_clicks_time)),NUM_UNIQUE(clicks.devices.MODE(clicks.ip)),NUM_UNIQUE(clicks.devices.MODE(clicks.app)),NUM_UNIQUE(clicks.devices.MODE(clicks.os)),NUM_UNIQUE(clicks.devices.MODE(clicks.channel)),NUM_UNIQUE(clicks.devices.DAY(first_clicks_time)),NUM_UNIQUE(clicks.devices.YEAR(first_clicks_time)),NUM_UNIQUE(clicks.devices.MONTH(first_clicks_time)),NUM_UNIQUE(clicks.devices.WEEKDAY(first_clicks_time)),NUM_UNIQUE(clicks.oses.MODE(clicks.ip)),NUM_UNIQUE(clicks.oses.MODE(clicks.app)),NUM_UNIQUE(clicks.oses.MODE(clicks.device)),NUM_UNIQUE(clicks.oses.MODE(clicks.channel)),NUM_UNIQUE(clicks.oses.DAY(first_clicks_time)),NUM_UNIQUE(clicks.oses.YEAR(first_clicks_time)),NUM_UNIQUE(clicks.oses.MONTH(first_clicks_time)),NUM_UNIQUE(clicks.oses.WEEKDAY(first_clicks_time)),NUM_UNIQUE(clicks.channels.MODE(clicks.ip)),NUM_UNIQUE(clicks.channels.MODE(clicks.app)),NUM_UNIQUE(clicks.channels.MODE(clicks.device)),NUM_UNIQUE(clicks.channels.MODE(clicks.os)),NUM_UNIQUE(clicks.channels.DAY(first_clicks_time)),NUM_UNIQUE(clicks.channels.YEAR(first_clicks_time)),NUM_UNIQUE(clicks.channels.MONTH(first_clicks_time)),NUM_UNIQUE(clicks.channels.WEEKDAY(first_clicks_time)),MODE(clicks.ips.MODE(clicks.app)),MODE(clicks.ips.MODE(clicks.device)),MODE(clicks.ips.MODE(clicks.os)),MODE(clicks.ips.MODE(clicks.channel)),MODE(clicks.ips.DAY(first_clicks_time)),MODE(clicks.ips.YEAR(first_clicks_time)),MODE(clicks.ips.MONTH(first_clicks_time)),MODE(clicks.ips.WEEKDAY(first_clicks_time)),MODE(clicks.devices.MODE(clicks.ip)),MODE(clicks.devices.MODE(clicks.app)),MODE(clicks.devices.MODE(clicks.os)),MODE(clicks.devices.MODE(clicks.channel)),MODE(clicks.devices.DAY(first_clicks_time)),MODE(clicks.devices.YEAR(first_clicks_time)),MODE(clicks.devices.MONTH(first_clicks_time)),MODE(clicks.devices.WEEKDAY(first_clicks_time)),MODE(clicks.oses.MODE(clicks.ip)),MODE(clicks.oses.MODE(clicks.app)),MODE(clicks.oses.MODE(clicks.device)),MODE(clicks.oses.MODE(clicks.channel)),MODE(clicks.oses.DAY(first_clicks_time)),MODE(clicks.oses.YEAR(first_clicks_time)),MODE(clicks.oses.MONTH(first_clicks_time)),MODE(clicks.oses.WEEKDAY(first_clicks_time)),MODE(clicks.channels.MODE(clicks.ip)),MODE(clicks.channels.MODE(clicks.app)),MODE(clicks.channels.MODE(clicks.device)),MODE(clicks.channels.MODE(clicks.os)),MODE(clicks.channels.DAY(first_clicks_time)),MODE(clicks.channels.YEAR(first_clicks_time)),MODE(clicks.channels.MONTH(first_clicks_time)),MODE(clicks.channels.WEEKDAY(first_clicks_time))\n" \
               "181628,12,1,17,245,2017-11-07 04:00:00,0,57.0,0.012016028564053744,1.0,83.19813681199888,0.0,0.00014440579548592551,394721.0,44122.0,4.0,126.0,27.0,73487.0,1.0,19.0,178.0,7.0,2017.0,11.0,1.0,1.0,1.0,1.0,1.0,7.0,2017.0,11.0,1.0,271861.0,7677.63149477453,100677.0,1745584.2592307085,1.0,881.2550456042827,160703909.0,8046655.0,843610.0,6714542.0,17701355.0,2901672588.0,19132.260517124592,394636.0,8470423.675463136,0.0,945.1956004237917,1171861222328.0,21076751459.0,63902363.0,63147711.0,62662513.0,390052565.0,18122.68087681511,392807.0,9053122.245292146,0.0,909.9710530699,156029847594.0,10088703287.0,36845080.0,1125693.0,54313349.0,10128946.0,6306.687586333697,385059.0,28528598.212958675,0.0,139.42323794385592,30775535370.0,8397967298.0,1004221.0,1275592.0,32465589.0,2.5347645871738775,0.04095945486329622,0.43589417107238476,9.377080887488868,0.001591674775270396,0.013099926307302105,1245.584920707449,8.579268042966298,1.8563172164966113,14.076771590022972,21.418923264613916,1464.6365159938853,0.006269584400594436,0.01467295483391525,7.289809235391754,0.0,0.00041969482303657923,576758.1584679061,9386.389904559313,20.570767680314088,10.202734245106228,6.375624315833873,914.3749426641835,0.013697023953368088,0.06946568834773595,6.236491070597218,0.0,0.0021117361722215004,337163.78159924666,14371.854696649934,24.80787324539839,0.36504211816146503,13.162891356868325,31.058705572736077,0.009200399973321751,0.15452790740496838,29.403334449268666,0.0,0.003628281390512949,37269.30035432613,6678.225225986462,1.0838788323394724,0.8408082222557437,14.06564712609969,27.0,0.5,1.0,75.7627888488495,1.0,1.0,11340.0,65.0,15.0,76.0,98.0,7644.0,0.04972270116976118,1.0,58.0010370345043,0.0,0.002478489923920346,3084136.0,55273.0,166.0,162.0,160.0,2161.0,0.20593103328399892,1.0,52.9433693346602,0.0,0.04437689969604863,797759.0,41183.0,167.0,4.0,150.0,732.0,0.43473779644984856,1.0,137.6335716777865,0.0,0.7939262472885033,128666.0,27907.0,13.0,73.0,110.0,6.762576012239319,3.333800119233473,1.1238570272418387,3.117495154090397,628.2658672906985,26.422364088488596,5.981791283299754,1.2244583745251922,3.2405812645390144,2.0265861506248495,0.2109333355706465,-4.802241908447311,-4.819242777672682,-68.12324629652187,4.800319535490621,0.0,-4.803153084707105,-4.802265724303549,-4.802684146918266,-4.813515769155208,-5.145073860371439,-5.655425816777559,0.18369491615585187,3.229302896767236,-14.255987874618716,0.8009074052404512,0.0,11.236341156659734,0.11239040029802502,-0.13866613850495246,-0.529162823482362,-2.158797970432705,-2.586034972746558,2.135785841229482,3.4302734983933747,-6.154512268148946,-0.1889309441045429,0.0,212.9498020072768,-0.5044279324508824,-1.1303814048167362,0.7950420523749139,1.0012165810864015,0.15345178874192214,0.0,0.0,0.0,-1.7888543819998328,0.0,0.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,252.0,113.0,17.0,3.0,40.0,0.0,0.0,0.0,0.0,0.0,0.0,2.0,1.0,2.0,1.0,2.0,0.0,0.0,0.0,-1.4533390590214743,0.0,0.0,67.0,18.0,1.0,1.0,8.0,0.6887421748526175,0.01945078041141599,0.2550586363532723,4.422324272665271,2.533435008525009e-06,0.002232602383973193,407.13290906741724,20.385677478522805,2.1372311075417825,17.01085576901153,44.84523245532921,7351.198917716564,0.04847033858630423,0.9997846580242754,21.459267876457385,0.0,0.0023945916240174494,2968834.245778664,53396.580012211154,161.8924835516732,159.98062175561978,158.7514041563535,988.1728233359765,0.0459126341816501,0.9951510053936832,22.935496832679654,0.0,0.002305352522591653,395291.4782694612,25559.07409790713,93.34461556390463,2.851870055051543,137.59933978683677,25.661026395859352,0.015977583119047876,0.9755219509476314,72.2753494568535,0.0,0.000353219712008877,77967.81871245767,21275.704353201374,2.544128637695993,3.231629429394433,82.24945974498443,48.0,8.0,88.0,112.0,1.0,1.0,1.0,1.0,3.0,3.0,3.0,3.0,1.0,1.0,1.0,1.0,108.0,9.0,3.0,26.0,1.0,1.0,1.0,1.0,12.0,10.0,2.0,3.0,1.0,1.0,1.0,1.0,3.0,1.0,19.0,280.0,7.0,2017.0,11.0,1.0,5348.0,3.0,19.0,280.0,7.0,2017.0,11.0,1.0,5348.0,3.0,1.0,280.0,7.0,2017.0,11.0,1.0,5348.0,12.0,1.0,19.0,7.0,2017.0,11.0,1.0"
        f = StringIO(scsv)
        for row in csv.DictReader(f):
            print(construct_line(row))
            # self.assertEqual("-1 |ip 87540 |app 12 |device 1 |os 13 |channel 497\n", construct_line(row))


if __name__ == '__main__':
    unittest.main()
