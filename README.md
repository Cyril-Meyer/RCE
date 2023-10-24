# RCE
This repository has **educational** purposes and includes videos and reports that I made to **archive** my research in **Reverse Code Engineering**.

If you are a beginner, I advise you to take a look at the **crackme** guides at the bottom of the list, the tables are filled in reverse chronological order.
The most basic explanations have been made on the simplest crackme and are not necessarily repeated.  
By starting this repository, I already have experience in the field, but we still start with fairly easy problems.

List of symbols used:
* 📜 Guide
* 📝 Memorandum
* 🔑 Keygen / Key
* ☠️ Crack / Patch
* 🧪 Analysis
* 🎥 Video
* 🔗 Source URL

## CrackMes

### [crackmes.one](https://crackmes.one/)

| Analysis | 🧲 | Name | Author | Language | Arch | Difficulty | Platform | Crackme Date |
|:---:|:---:|:----:|:------:|:--------:|:----:|:----------:|:--------:|:----:|
|[📜☠️](crackme/6522ff948b6aa566ae723692.md)|[🔗](https://crackmes.one/crackme/6522ff948b6aa566ae723692)| PrimeKey Puzzle | PyroDeathAdder | C/C++ | x86 | 3.0 | Unix/linux | 10/08/2023 |
|[📜🔑](crackme/651db8f78b6aa566ae7234ec.md)|[🔗](https://crackmes.one/crackme/651db8f78b6aa566ae7234ec)| My first Crackme (Write a keygen) | sc0rp10n | C/C++ | x86-64 | 2.0 | Unix/linux | 10/04/2023 |
|[📜🔑](crackme/6522cc2f8b6aa566ae72366c.md)[🎥](https://www.youtube.com/watch?v=k9nHvJ5AZ7g)|[🔗](https://crackmes.one/crackme/6522cc2f8b6aa566ae72366c)| MasonCrackme | ABOLHB | .NET | x86-64 | 4.0 | Windows | 10/08/2023 |
|[📜🔑](crackme/64fb27f4d931496abf909849.md)[🎥](https://www.youtube.com/watch?v=6LuIlvtA9Z4)|[🔗](https://crackmes.one/crackme/64fb27f4d931496abf909849)| Freemasonry | ABOLHB | .NET | x86-64 | 2.0 | Windows | 09/08/2023 |
|[📝🔑](crackme/64e22875d931496abf908fdb.md)[🎥](https://www.youtube.com/watch?v=OIdSNTQ8ELI)|[🔗](https://crackmes.one/crackme/64e22875d931496abf908fdb)| skStr() crackme | C0pl3x | C/C++ | x86-64 | 2.0 | Windows | 08/20/2023|
| | | | | | | | | |

## Malware

| Analysis | Name (hash) | Language / Arch | Date |
|:--------:|:----:|:---------------:|:----:|
|[🧪](malware/f4e3282da56f5722c44c6b60c3792674ec3aa322.md)| f4e3282da56f5722c44c6b60c3792674ec3aa322 | Windows .NET | 2014 |



## Tools
I may mention names of tools in different guides, here is a list of most of the tools used with a link to download them as well as the features for which I find them useful.

* [x64dbg](https://x64dbg.com/) : disassembler and debugger for windows PE target
  * [snowman](https://github.com/x64dbg/snowman) : decompiler plugin
* [IDA free](https://hex-rays.com/ida-free/) : disassembler, debugger and decompiler for windows and linux (debugger only work on same system)
* [dnSpy](https://github.com/dnSpy/dnSpy) : decompiler and debugger for .NET
* [cutter](https://cutter.re/) : decompiler and debugger for linux ELF target
