import random
import numpy as np
import time
import sys
students=['이대원','김동현','송승호','장은경','조석현','서자빈','이창기','전호연','정상훈',\
    '전이훈','강석희','권세종','김명주','이소현','박우석','정  웅','오성준','이대현','이석연',\
    '전제민','김상혁','성민혁','김수현','정지훈','이나연']

random.shuffle(students)

row=int(sys.argv[1])

if row==6: #6*5:
    students+=[None]*(30-len(students))
    a=np.array(students).reshape(5,6)

elif row==7: #7*4:
    students+=[None]*(28-len(students))
    a=np.array(students).reshape(4,7)

print(f"\n실행시점: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
print("\n===================== 첫 줄 비우기 =====================")
print(a)