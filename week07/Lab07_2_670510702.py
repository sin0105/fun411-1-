#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab07_2
# 204111 Sec 003

def main():
    square_frame(5,'.')
    '''
			  01.02.03.04.05 ->ranger
	tlast ->(16)..........06 |
			  15..........07 |-rangee
			  14..........08 |
	blast ->(13).12.11.10.09 ->rangey

    '''

def square_frame(n: int, sep: str=' '):
    tlast = len(str((n**2)-((n-2)**2)))         
    blast = (n**2)-((n-2)**2)-(n-2)
    ranger = list(range(1,n+1))
    rangee = list(range(1,n-1))
    rangey = list(range(blast,n+(n-2),-1))

    tnum = list(map(lambda rg: str(rg).zfill(tlast),ranger))                 # ตัวเลขแถวบน .zfill(ตามจำนวน tlast)
    tnum_final = (str(tnum).strip('[]').replace(', ',sep).replace("'",''))   # (เอา[]ออก) (แทนที่ , ด้วย sep) (แทนที่ ' ด้วย '') 


    dot = list(map(lambda re: str(((n**2)-(n-2)**2)+(1-re)).zfill(tlast) + sep*((n-1)+(n-2)*tlast) + str(n+re).zfill(tlast),rangee))
    dot_final = str(dot).strip('[]').replace("'",'').replace(', ','\n')
    '''
    																		dot = (ตัวที่ tlast + (1-รอบของrangee)).zfill(ตามจำนวน tlast) 
    																				+ ใส้กลาง sep*สูตร
																					+ (n-รอบของrangee).zfill(ตามจำนวน tlast) 
    '''
    
    bnum = list(map(lambda ry: str(ry).zfill(tlast),rangey))				 # ตัวเลขแถวล่าง .zfill(ตามจำนวน tlast)
    bnum_final = (str(bnum).strip('[]').replace(', ',sep).replace("'",''))   # (เอา[]ออก) (แทนที่ , ด้วย sep) (แทนที่ ' ด้วย '') 
    
    print(tnum_final+'\n'+dot_final+'\n'+bnum_final)

   
if __name__ == '__main__':
    main()
