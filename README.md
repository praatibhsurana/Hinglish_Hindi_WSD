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
1) **A small change will need to be made to iwn.py from the pyiwn library before using our package** <br> 

- There is a missing try-catch block in iwn.py that might cause our package to crash 
- Here's a quick fix, use our patched [iwn.py](https://github.com/praatibhsurana/pyiwn/blob/patch-1/pyiwn/iwn.py) instead. Copy it's contents and replace the original iwn.py. 
- The path to the original iwn.py would be **path-to-your-env-or-python-folder/lib/site-packages/pyiwn/iwn.py**

<br>

## 📄 CUSTOM DATASET FOR ENHANCED LESK'S ALGORITHM
**The custom dataset is available [here](https://github.com/praatibhsurana/Hinglish_Hindi_WSD/tree/main/dataset).**
- Here is a preview of what it looks like <br><br>
![image](https://user-images.githubusercontent.com/43675042/150093498-056089b4-a957-4c7e-8f32-875d296a353d.png)


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

## Citing

If you publish work that uses hindiwsd, please cite the hindiwsd paper, as follows:

```latex
@InProceedings{yusuf-surana-sharma:2022:WILDRE6,
  author    = {Yusuf, Mirza  and  Surana, Praatibh  and  sharma, Chethan},
  title     = {HindiWSD: A package for word sense disambiguation in Hinglish \& Hindi},
  booktitle      = {Proceedings of The WILDRE-6 Workshop within the 13th Language Resources and Evaluation Conference},
  month          = {June},
  year           = {2022},
  address        = {Marseille, France},
  publisher      = {European Language Resources Association},
  pages     = {18--23},
  abstract  = {A lot of commendable work has been done, especially in high resource languages such as English, Spanish, French, etc. However, work done for Indic languages such as Hindi, Tamil, Telugu, etc is relatively less due to difficulty in finding relevant datasets, and the complexity of these languages. With the advent of IndoWordnet, we can explore important tasks such as word sense disambiguation, word similarity, and cross-lingual information retrieval, and carry out effective research regarding the same. In this paper, we worked on improving word sense disambiguation for 20 of the most common ambiguous Hindi words by making use of knowledge-based methods. We also came up with â€œhindiwsdâ€, an easy-to-use framework developed in Python that acts as a pipeline for transliteration of Hinglish code-mixed text followed by spell correction, POS tagging, and word sense disambiguation of Hindi text. We also curated a dataset of these 20 most used ambiguous Hindi words. This dataset was then used to enhance a modified Lesk's algorithm and more accurately carry out word sense disambiguation. We achieved an accuracy of about 71\% using our customized Leskâ€™s algorithm which was an improvement to the accuracy of about 34\% using the original Leskâ€™s algorithm on the test set.},
  url       = {https://aclanthology.org/2022.wildre6-1.4}
}
```


### Feel free to reach out to us for more information!
- [Praatibh Surana](https://github.com/praatibhsurana)
- [Mirza Yusuf](https://github.com/YusufBaig7)
