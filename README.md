# How to install VSCode as Portable in a Remobvable Disk(Pendrive) or something along those lines.

*** Before installing and doing anything, kindly read the whole thing once. It won't take more than 15 minutes at maximum, so as to to not mess up any stuff along the way.*** Thank You

## Installing Portable VSCode
### First Step : 
Install your preferred .zip version from https://code.visualstudio.com/download and extract it to the Removable Disk


### Second Step :
Create a new folder named "data" in  in the path where the extracted .exe file lies in.
Then create two subfolders inside "data" and name it as "user-data" and "extensions"

This is how it should look like:
|- VSCode-win32-x64-1.25.0-insider
|   |- Code.exe (or code executable)
|   |- data
|   |   |- user-data
|   |   |   |- ...
|   |   |- extensions
|   |   |   |- ...
|   |- ...
 
Or Jump to [How I have done them](#-How-I-have-structured-them-with-images:) to look at how I did it.


### Third Step :
->Now in "user-data" folder paste the following files when you run "%APPDATA%\Code" or you can do it the old fashioned way. 
Go to "C:\Users\'YourUserName'\AppData\Roaming\Code" and paste everything there to the user-data folder in Removable Disk

->Now in "extensions" folder paste the following when you run "%USERPROFILE%\.vscode\extensions" or you can do it the old fashioned way. 
Go to "C:\Users\'YourUserName'\.vscode\extensions" and paste everything there to the extensions folder in Removable Disk


## How to structure the compilers into folders
I wrote the code as per *my convenience*, you *can change* the path to your preference.
And this is what my drive looks like:
(Again while I would like to *emphasize* that you can structure it in any way, just make sure it is reflected in the script too)
Sam's Drive
|-VSCode
|  |-CODE
|  |  |-..Portable VSCode extracted into this folder
|  |-compilers
|  |  |-MinGW
|  |  |  |-bin
|  |  |-jdk-17
|  |  |  |-...
|  |  |-Python39
|  |  |  |-...


### How I have structured them with images:
My Removable Disk:
/assets/Screenshots/1.Drive.png

Contents of 'VSCode' folder:
/assets/Screenshots/2.0.VSCode.png

Contents of 'CODE'(Contains VSCode's exe, i.e the portable vscode which was downloaded in the `First Step`):
/assets/Screenshots/2.1.0.CODE.png

Contents of 'data' in CODE(Things which we created in `Second Step`):
/assets/Screenshots/2.1.1.0.VSCode_data

Contents of 'user-data'(which we created in `Third Step`) in data:
/assets/Screenshots/2.1.1.1.data_user-data.png

Contents of 'extensions'(`Third Step`, I know I have a lot of extensions,Just wanted to make sure they work)-
/assets/Screenshots/2.1.1.2.Code_Extensions

Contents of 'Compilers' folder:
/assets/Screenshots/2.2.0.Compilers.png

Contents of 'jdk':
/assets/Screenshots/2.2.1.jdk.png

Contents of 'MinGW':
/assets/Screenshots/2.2.2.MinGW.png

Contents of 'Python39':
/assets/Screenshots/2.2.3.Python.png


### MinGW gcc/g++ compilers:
Just download it from the SourceForge link as per your requirements from : https://www.mingw-w64.org/downloads/#mingw-builds
Then extract it to your preferred folder as per the code.

### Python:
Install it on your system and then copy the whole folder from where you have installed it. Or download it straight up into the removable drive.

### jdk(Java)
Yeah, same as python. Install it and then copy or just straight up download it into the removable drive.


## How to Run the exe file:
Open the terminal and run the exe file.
Image on how to use it:
/assets/Screenshots/exefile.png

`I think it is self-explanatory.`


### Or just download from the google drive links which I have probably provided, if not then I may have forgotten about that.


*I'll include snapshots in assets folder or inside the readme file itself to get a clear view on how the files are meant to be saved*

*I didnt require other compilers/interpreters while writing this piece so I haven't researched on how other interpreters/compilers work.* Thank You.


#### Misc.:
I used ShareX for the screenshots.
