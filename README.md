# heconsole
#### Perfect pip module to design and display your terminal, great customization

## Installation
```
// Installation this module is not difficult, 
// just write the command below.

pip install heconsole
```

## Usage
#### this pip module has a lot of useful things for customization and logging

```python
from heconsole import console
console.setTimeFormat(timeFormat='%H:%M:%S')

console.log(0, "log")
console.warn(0, "warn")
console.error(0, "error")
console.success(0, "success")
console.info(0, "info")
console.revers(0, "revers log + detail")
console.detail(0, "detailed log")
console.dir(0, "this log with dir")

console.arrowLog(0, "arrow log")
console.arrowWarn(0, "arrow warn")
console.arrowError(0, "arrow error")
console.arrowSuccess(0, "arrow success")
console.arrowInfo(0, "arrow info")
console.arrowRevers(0, "arrow revers")
console.arrowDetail(0, "arrow detail")
console.arrowDir(0, "arrow dir ")

console.log(0, "no .GREENdate.WHITE time ;-)", showTime=False)
console.success(0, ".YELLOWyellow & .GREENgreen color.WHITE MAGENTABGmagenta bg ", showTime=False)

console.bold(0, "bold text")
console.italic(0, "italic text")
console.inverse(0, "inverse text")
console.underline(0, " underline text")
console.log(2, "wait 2 secons to print") # times 2 secs

# or
console.arrowLog(0, ".BOLD bold .ITALICitalic .INVERSE inverse .UNDERLINE underline")

# example
console.arrowLog(0, ".BOLD Lorem .GREENipsum dolor .ITALIC sit amet,.BLACK REDBGconsectetur adipiscing .BLUEelit...")
```

## Output
<img width="99.9%" src="https://raw.githubusercontent.com/mishakorzik/heconsole/main/images/IMG_20220806_222355.jpg"/>

customizing the log entry terminal.
