## Email Dataset
```
                                          Email Text      Email Type
0  Dear Jordan, your subscription has been succes...      Safe Email
1  Dear Casey, thank you for your purchase. Your ...      Safe Email
2  Congratulations! You've won a $3000 gift card....  Phishing Email
3  You have a new secure message from your bank. ...  Phishing Email
4  Your package delivery is pending. Please provi...  Phishing Email

Total rows: 2000

Class distribution:
Email Type
Safe Email        1000
Phishing Email    1000
Name: count, dtype: int64

Missing values per column:
Email Text    0
Email Type    0
dtype: int64
```

## URL dataset
Columns:
```
Index(['FILENAME', 'URL', 'URLLength', 'Domain', 'DomainLength', 'IsDomainIP',
       'TLD', 'URLSimilarityIndex', 'CharContinuationRate',
       'TLDLegitimateProb', 'URLCharProb', 'TLDLength', 'NoOfSubDomain',
       'HasObfuscation', 'NoOfObfuscatedChar', 'ObfuscationRatio',
       'NoOfLettersInURL', 'LetterRatioInURL', 'NoOfDegitsInURL',
       'DegitRatioInURL', 'NoOfEqualsInURL', 'NoOfQMarkInURL',
       'NoOfAmpersandInURL', 'NoOfOtherSpecialCharsInURL',
       'SpacialCharRatioInURL', 'IsHTTPS', 'LineOfCode', 'LargestLineLength',
       'HasTitle', 'Title', 'DomainTitleMatchScore', 'URLTitleMatchScore',
       'HasFavicon', 'Robots', 'IsResponsive', 'NoOfURLRedirect',
       'NoOfSelfRedirect', 'HasDescription', 'NoOfPopup', 'NoOfiFrame',
       'HasExternalFormSubmit', 'HasSocialNet', 'HasSubmitButton',
       'HasHiddenFields', 'HasPasswordField', 'Bank', 'Pay', 'Crypto',
       'HasCopyrightInfo', 'NoOfImage', 'NoOfCSS', 'NoOfJS', 'NoOfSelfRef',
       'NoOfEmptyRef', 'NoOfExternalRef', 'label'],
      dtype='object')
```
Rows:
```
     FILENAME                                 URL  URLLength                      Domain  DomainLength  IsDomainIP  TLD  ...  NoOfImage  NoOfCSS  NoOfJS  NoOfSelfRef  NoOfEmptyRef  NoOfExternalRef  label
0  521848.txt    https://www.southbankmosaics.com         31    www.southbankmosaics.com            24           0  com  ...         34       20      28          119             0              124      1
1   31372.txt            https://www.uni-mainz.de         23            www.uni-mainz.de            16           0   de  ...         50        9       8           39             0              217      1
2  597387.txt      https://www.voicefmradio.co.uk         29      www.voicefmradio.co.uk            22           0   uk  ...         10        2       7           42             2                5      1  
3  554095.txt         https://www.sfnmjournal.com         26         www.sfnmjournal.com            19           0  com  ...          3       27      15           22             1               31      1  
4  151578.txt  https://www.rewildingargentina.org         33  www.rewildingargentina.org            26           0  org  ...        244       15      34           72             1               85      1  

[5 rows x 56 columns]

```