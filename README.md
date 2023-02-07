# Kindle Notes to Test Questions

Takes quotes from any kindle book and creates test questions and answers to help you remember the content of the book.

## Description

When you highlight a quote on a kindle, it will save the quote to your goodreads account as a "highlight". Since these are the most important parts of the book as determined by you, those are the "answers", or parts that we want to remember. In the software, I webscraped the quotes from the goodreads page you give me, and then run them through the OpenAI GPT-3 API to get test questions. Then, I give you back two .txt files: one containing just the questions (like a test), and one containing the questions and answers (like a cheat sheet). Enjoy your reading... and remembering!

## Getting Started

### Dependencies

Libraries Needed (pip or pip3 install):
* Beautiful Soup 4
* OpenAI

Languages:
* Python3

### Installing

Download all of the files, and make sure they are located in the same directory. Make sure Python3 is installed on your computer, and the BeautifulSoup4 and OpenAI packages have been installed.

For Beautiful Soup 4:
```
pip install beautifulsoup4
```
or if you use pip3:
```
pip3 install beautifulsoup4
```

For OpenAI:
```
pip install openai
```
or if you use pip3:
```
pip3 install openai
```



### Executing program

In the terminal, navigate to the directory containing the files and enter:
```
python3 main.py
```
Make sure your goodreads page for the certain book is set to "visible". Then, enter your goodreads page URL when prompted. After giving a few seconds to load, the resulting files should be in the same directory, one with questions, and one with questions and answers.

## Author

Trent Kelly 
trentjkelly@outlook.com

## Version History

* 1.0 
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration:
* [nicolasdao](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [Ali Abdaal - Active Recall](https://www.youtube.com/watch?v=fDbxPVn02VU)