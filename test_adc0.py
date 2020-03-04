import devmem
base=0xff200000
adcChanel0=devmem.DevMem(base, 0x100, "/dev/mem", 0)
adcValue=adcChanel0.read(0,1)[0]
print("adc ch 0: %d " % adcValue)
 
