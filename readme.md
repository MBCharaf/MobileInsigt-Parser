# MobileInsight Parser
This is a parser for Mobileinsight exported xml files. It supports JSON and CSV as output files.

## Usage
In parse.py spcify the target file and the message that you want to parse as:
```python
Parser = LteParser("lte-test.xml","LTE_PHY_Connected_Mode_Intra_Freq_Meas")
```
## Run
```bash
python3 parse.py
```
Two output files are going to be generated as .csv and .json

