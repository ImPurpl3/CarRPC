# CarRPC
Discord Rich Presence for Red Ball Hacks

# How to install
* In the folder that you have your Flash Player.exe (Projector) in, make a subfolder called "fscommand" and place CarRPC.exe inside of it. 
* If you want to use command line arguments, it would be wise to make a batch file named "CarBAT.bat" and put it in the same folder as the "CarRPC.exe" 

![Example](https://i.imgur.com/DHQRDd2.png)
![Example](https://i.imgur.com/o4ETYiA.png)

# Compiling
Use pyinstaller and cd to the directory that the main python script is in then type or copy in this command:
```
pyinstaller -i "car.ico" ^ -n "CarRPC" ^ --onefile ^ "car.py"
```

# Implementing
__You will need a good understanding of ActionScript to implement this into your own hack__

The following gets the Flash Cookie for use of the RPC:
```
var rpcSet:SharedObject;
rpcSet = SharedObject.getLocal("rpc","/");
```
> Dont forget to put the *"/"* after the *"rpc"* or else it wont save to the local cookie folder

To check if the setting is on to run the program:
```
if (rpcSet.data.setting == "On") {
  fscommand("exec","CarRPC.exe");
}
```
Add your own code as needed

# Arguments
```
usage: CarRPC.exe [-h] [-s SOLPASS] [-i IDPASS] [-x MAXPASS] [-m MINPASS]

optional arguments:
  -h, --help            show this help message and exit
  -s SOLPASS, --sol SOLPASS
                        Name of SOL to Load
                        
  -i IDPASS, --appid IDPASS, --id IDPASS
                        Discord App ID
                        
  -x MAXPASS, --max MAXPASS
                        Maximum # of Levels
                        
  -m MINPASS, --min MINPASS
                        Minimum # of Levels
```       
# Other Things to Note
* Only works on Windows
* When changing file types in the Settings menu, you might have to turn the setting off and on again
* When compiling, have the icon in the same folder as the main python script
