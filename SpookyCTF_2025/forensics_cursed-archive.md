## **Cursed-Archive**

### **Challenge Information**

<p align="center">
  <img src="assets/cursed-archive/cursed-archive.png" width="420" alt="Screenshot of 'Cursed-Archive' challenge card">
</p>

#### **Challenge Files**

[gargoyle.txt](assets/cursed-archive/gargoyle.txt)

### **Solution**

I first tried to open the txt file only to see a bunch of nonsense. After that, I ran `file gargoyle.txt` and got this:

![filegargoyle.png](assets/cursed-archive/filegargoyle.png)

From here, I knew that gargoyle.txt was actually a gzip file, not a txt file, so I renamed it gargoyle.gz and unzipped it. Unzipping gave me a foleder with 3 files, `file1`, `file2.gz`, and `file3.gz`. `file1` said "You're Onto Something!". After unzipping `file2.gz`, I ended up with a file named `file2`, which said "Keep Going!". After unzipping `file3.gz`, I got a file named `file3` which said "flag found: NICC{tAr_gZip_eXtrActEd}" and that is the flag.

The flag is: `NICC{tAr_gZip_eXtrActEd}`