# self.CL1 = self.ui.lineCL1
# self.CL2 = self.ui.lineCL2
# self.CL3 = self.ui.lineCL3
# self.CL4 = self.ui.lineCL4
# self.LT1 = self.ui.lineLT1
# self.LT2 = self.ui.lineLT2
# self.LT3 = self.ui.lineLT3
# self.LT4 = self.ui.lineLT4
# self.LT5 = self.ui.lineLT5
# self.LT6 = self.ui.lineLT6
# self.WT1 = self.ui.lineWT1
# self.WT2 = self.ui.lineWT2
# self.WT3 = self.ui.lineWT3
# self.WT4 = self.ui.lineWT4
sens_pos = dict.fromkeys(
['CL1', 'CL2', 'CL3', 'CL4', 'LT1', 'LT2',
'LT3', 'LT4', 'LT5', 'LT6', 'WT1', 'WT2',
'WT3', 'WT4', 'WT5', 'WT6', 'TEMP1', 'TEMP2',
'PRES1', 'PRES2'], 0
)
sens_pos['CL', 'CT'] = 1
s = sens_pos.values()
print(sens_pos)
