
:: shadow_maya is determined by the current folder name
for %%I in (.) do set shadow_maya=%%~nxI
SET CLEAN_shadow_maya=%shadow_maya:-=_%

:: Check if modules folder exists
if not exist %UserProfile%\Documents\maya\modules mkdir %UserProfile%\Documents\maya\modules

:: Delete .mod file if it already exists
if exist %UserProfile%\Documents\maya\modules\%shadow_maya%.mod del %UserProfile%\Documents\maya\modules\%shadow_maya%.mod

:: Create file with contents in users maya/modules folder
(echo|set /p=+ %shadow_maya% 1.0 %CD%\_setup_\maya & echo; & echo icons: ..\%CLEAN_shadow_maya%\icons)>%UserProfile%\Documents\maya\modules\%shadow_maya%.mod

:: end print
echo .mod file created at %UserProfile%\Documents\maya\modules\%shadow_maya%.mod



