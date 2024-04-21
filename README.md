- First You Need Like This
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/YfwfxQOMQOGRM4q6W02NEw.png)](https://github.com/ylasgamers/mint.club)

- After Need Install Extension Python Like This
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/tjRxiDmZSpCQB4qoBPZO8A.png)](https://github.com/ylasgamers/mint.club)

- Next Install Requirements On Terminal And Enter
```
python -m pip install -r requirements.txt
```
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/gIaz5LBHSkS7esvxY4Lpqw.png)](https://github.com/ylasgamers/mint.club)

- After This You Need Edit/Change RPC Url, ChainID You Can Find On [chainlist.org](https://chainlist.org) or [thirdweb.com/chainlist](https://thirdweb.com/chainlist) On claimerc20.py
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/OEYOWMdsSdW3ntZRG3SbPw.png)](https://github.com/ylasgamers/mint.club/blob/72a4e89462df76337eb88cb37550aa1566d4c055/claimerc20.py#L8)

- Next You Need Edit merkleaddr, & Add/Remove Address & Privatekey To Using Claim On claimerc20.py
```
choose chain you want to enabled, pick only one
just remove # if you want enabled, and add # if you want disabled
#degen
merkleaddr = web3.to_checksum_address("0x5DaE94e149CF2112Ec625D46670047814aA9aC2a")
#base / arbitrum / bsc or bnb / ethereum / optimistic / polygon
#merkleaddr = web3.to_checksum_address("0x1349a9ddee26fe16d0d44e35b3cb9b0ca18213a4")
#avalanche
#merkleaddr = web3.to_checksum_address("0x841A2bD2fc97DCB865b4Ddb352540148Bad2dB09")
#blast
#merkleaddr = web3.to_checksum_address("0x29b0E6D2C2884aEa3FB4CB5dD1C7002A8E10c724")
#klaytn / zora
#merkleaddr = web3.to_checksum_address("0x3bc6b601196752497a68b2625db4f2205c3b150b")
#sepolia
#merkleaddr = web3.to_checksum_address("0x0CD940395566d509168977Cf10E5296302efA57A")

you can add/remove address & privatekey here
MultiClaim(web3.to_checksum_address("0xyouraddr1"), "yourpvkey1")    
MultiClaim(web3.to_checksum_address("0xyouraddr2"), "yourpvkey2")
```

[![YLAS GAMERS](https://img001.prntscr.com/file/img001/vHjNpOeVSKGhQ1JQtG6HhA.png)](https://github.com/ylasgamers/mint.club/blob/72a4e89462df76337eb88cb37550aa1566d4c055/claimerc20.py#L19)
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/PAk0vdqLRDySoq_8uK4jfg.png)](https://github.com/ylasgamers/mint.club/blob/72a4e89462df76337eb88cb37550aa1566d4c055/claimerc20.py#L59)

- After This, You Can Run python claimerc20.py
- You Need Know DistributionId For Claim Airdrops On [mint.club](https://mint.club/airdrops)
- How To Find DistributionId ??? Look Below
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/BG4XUCoVRfeARsRGVhjBPw.png)](https://github.com/ylasgamers/mint.club)
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/d0n7u3bwTBmjZtyJITQzfA.png)](https://github.com/ylasgamers/mint.club)
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/oAjH-4BTQWuSq2xuxCjMKg.png)](https://github.com/ylasgamers/mint.club)
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/Be21L_oQRdyTQaOJhZhr7Q.png)](https://github.com/ylasgamers/mint.club)
- For Some Explorer Chain 3 Image Same, But Last Image Litle Different, So Look Below
- For Example On Explorer Base Chain
[![YLAS GAMERS](https://img001.prntscr.com/file/img001/EOjen8WvSxe1byMZ8xvHSg.png)](https://github.com/ylasgamers/mint.club)
