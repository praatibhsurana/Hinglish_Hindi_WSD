<p>  
  <a href="https://github.com/praatibhsurana/Hinglish_Hindi_WSD/stargazers">  
    <img src="https://img.shields.io/github/stars/praatibhsurana/hinglish_hindi_wsd.svg?colorA=orange&colorB=orange&logo=github"  
         alt="GitHub stars">  
  </a> 
  <a href="https://pypi.org/project/hindiwsd/">  
      <img src="https://img.shields.io/pypi/v/hindiwsd?colorB=brightgreen" alt="Pypi package">  
  </a>  
  <a href="https://github.com/praatibhsurana/Hinglish_Hindi_WSD/issues">
        <img src="https://img.shields.io/github/issues/praatibhsurana/hinglish_hindi_wsd.svg"
             alt="GitHub issues">
  </a>
  <a href="https://github.com/praatibhsurana/Hinglish_Hindi_WSD/blob/main/LICENSE">  
        <img src="https://img.shields.io/github/license/praatibhsurana/hinglish_hindi_wsd.svg"  
             alt="GitHub license">  
  </a>
</p>  
  
<p> 📌 A pipeline for transliteration of Hinglish code mixed data to Hindi Devanagari script, spell correction, POS tagging and word sense disambiguation of the Hindi Devanagari script.       
</p>  

<p>  
📖 With this package, we aim to tackle the problem of word sense disambiguation by making atleast the preliminary steps a lot easier. The problem statement we decided to tackle was the translation of Hinglish code mixed data to Hindi Devanagari and then to carry out word sense disambiguation on the Hindi text. We make use of libraries such as <a href='https://github.com/hellohaptik/spello'>spello</a>, <a href='https://github.com/indic-transliteration/indic_transliteration_py'>indic-transliteration</a>, <a href='https://github.com/riteshpanjwani/pyiwn'>pyiwn</a> and <a href='https://github.com/avineshpvs/indic_tagger'>indic_tagger</a>.   
</p>  <br>

## 💡 Functionalities

**hindiwsd will mainly carry out the following tasks for now:**

- Hinglish to Hindi transliteration 
- Spell correction of Hindi text
- POS tagging of Hindi text 
- Word Sense Disambiguation of Hindi text with the help of IndoWordNet
- Enhanced Lesk's Algorithm using custom dataset

<br>

## 💾 Installation 
**Install hindiwsd via 'pip'**
```bash  
pip install hindiwsd
```  

<br>

## 🗒️ NOTE
1) **Use our pretrained models for POS tagging and Hindi spell correction to ensure hindiwsd works**

- [hi.pkl](https://github.com/praatibhsurana/Hinglish_Hindi_WSD/blob/main/src/hinglish-hindi-wsd/hi.pkl)
- [crf.pos.utf.model](https://github.com/praatibhsurana/Hinglish_Hindi_WSD/blob/main/src/hinglish-hindi-wsd/crf.pos.utf.model) <br>
**Download these models and paste them in the directory in which you are running your Python scripts** <br><br>

2) **A small change will need to be made to iwn.py from the pyiwn library before using our package** <br> 
**(The patch was merged to the original repo, YOU CAN SKIP THIS STEP)**
- There is a missing try-catch block in iwn.py that might cause our package to crash 
- Here's a quick fix, use our patched [iwn.py](https://github.com/praatibhsurana/pyiwn/blob/patch-1/pyiwn/iwn.py) instead. Copy it's contents and replace it with the original iwn.py. 
- The path to the original iwn.py would be **path-to-your-env-or-python-folder/lib/site-packages/pyiwn/iwn.py**

<br>

## 📄 CUSTOM DATASET FOR ENHANCED LESK'S ALGORITHM
**The custom dataset is available [here](https://github.com/praatibhsurana/Hinglish_Hindi_WSD/tree/main/dataset)**

<br>

## ⚡Getting Started
### 🔤 Word Sense Disambiguation
- **The wordsense() function from the hindi_wsd.py script.** 
**It prints out the Hindi Devanagari spell corrected sentence, POS tags and disambiguated word meanings for each word in the sentence available on the [IndoWordNet](https://www.cfilt.iitb.ac.in/indowordnet/).** 

```python  
>>> from hindiwsd import hindi_wsd  
>>> print(hindi_wsd.wordsense("aaj achha din hai"))   
```  

- **You can also directly feed in Hindi sentences to the wordsense() function.**
```python  
>>> from hindiwsd import hindi_wsd  
>>> print(hindi_wsd.wordsense("आज अच्छा दिन है"))   
```

<br>

### 🏷️ POS tagging for Hindi Devanagari
- **Getting POS tags for a Hindi sentence using the POS_tagger() function from the wsd.py script. Returns a list of tuples containing word and respective tag(NOUN, ADJECTIVE, ADVERB, VERB).**
```python  
>>> from hindiwsd import wsd  
>>> print(wsd.POS_tagger('आज अच्छा दिन है'))   
```

<br>

### 📚 Hinglish to Hindi transliteration with spell correction
- **Transliterating the Hinglish code mixed sentence to Hindi Devanagari using the preprocess_transliterate() function from the wsd.py script. Returns two strings. The first is the spell corrected Hinglish sentence followed by the spell corrected Hindi sentence.** 
```python  
>>> from hindiwsd import wsd  
>>> print(wsd.preprocess_transliterate('aaj achha din hai'))   
```

### Feel free to reach out to us for more information!
- [Praatibh Surana](https://github.com/praatibhsurana)
- [Mirza Yusuf](https://github.com/YusufBaig7)
