if (-not(([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))) {
    Start-Process powershell.exe  -Verb runas -ArgumentList "-NoExit", "-Command", "Set-ExecutionPolicy -Scope Process Bypass;", "&", $MyInvocation.MyCommand.Path;
    exit;
}

reg import reg

$code1 = Get-ItemProperty('hklm:\\Software\\Mandiant\\CTF')|Select-Object -ExpandProperty Mackerel;
echo "`r`n###code1###`r`n";
echo $code1;
$code2 = iex($code1.Replace('iex', 'echo'));
echo "`r`n###code2###`r`n";
echo $code2;
$code3 = iex($code2.Replace('iex', 'echo'));
echo "`r`n###code3###`r`n";
echo $code3;
$code4 = iex($code3.Replace('.  ${#}  (', ". echo ("));
echo "`r`n###code4###`r`n";
echo $code4;
$code5 = iex($code4.Replace('iex', 'echo'));
echo "`r`n###code5###`r`n";
echo $code5;

Remove-Item('hklm:\\Software\\Mandiant\\CTF');
