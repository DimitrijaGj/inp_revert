$inputString = '805CCB46444201'
$stringLength = $inputString.Length

for ($i = 0; $i -lt $stringLength; $i += 2) {
    $pair = $inputString.Substring($i, 2)
    $array = @()
    $array.Add($pair)
    Write-Output $array
}
