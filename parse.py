# Possible messsage to parse
#LTE_PHY_Connected_Mode_Intra_Freq_Meas
#LTE_PHY_Serv_Cell_Measurement
#LTE_PHY_Connected_Mode_Neighbor_Measurement

from MiParser import MiParser


if __name__=="__main__":
    Parser = MiParser("lte-test.xml","LTE_PHY_Connected_Mode_Intra_Freq_Meas")
    Parser.run()
