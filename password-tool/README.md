# Password Generator \& Strength Check



A simple command-line tool written in Python that generates random passwords and rates the strength of existing ones.



This is a learning project built to practice Python fundamentals and basic secure-coding concepts.



### Features



Password generator: creates random passwords of any length of 8 or more characters, using lowercase letters, uppercase letters, digits, and symbols

Strength checker:   rates a password on a 5-level scale, from Very Weak to Very Strong

Input validation:   invalid or too-short lengths are rejected and the user is asked again

Menu interface:     simple text menu that loops until you choose to exit



Requirements:

Python 3.6 or newer (uses only the standard library, so there is nothing to install)



### Run the script:



python password\_tool.py



You will see a menu:



1\. Generate Password

2\. Check Password Strength

3\. Exit





### How it works



#### Generator



Passwords are built with Python's secrets module, which draws from the operating system's cryptographically secure random source. The standard random module is deliberately not used because it's a predictable pseudo-random generator and is not suitable for security-sensitive values like passwords.



#### Strength checker



The checker is score-based. It adds or removes points for:



Length of 6 or fewer	        -1

Length of 8 or more	        +1

Length of 12 or more         	+1

Contains a lowercase letter	+1

Contains an uppercase letter	+1

Contains a digit	        +1

Contains a symbol       	+1



The total score is then mapped to a level from 1 (Very Weak) to 5 (Very Strong).



## Limitations



Please read these before relying on the checker for anything real:



The checker measures composition, not true strength. It only looks at length and character types. It does not detect common passwords, dictionary words, keyboard patterns (qwerty), sequences (12345678), or predictable substitutions (p@ssw0rd). For example, Password1! is rated "Very Strong" even though it is easily guessable.



It does not check against breached-password lists.



Generated passwords are not guaranteed to contain every character type. Characters are chosen at random, so a short password could, by chance, lack a digit or symbol.



Passwords are printed to the terminal. They are not stored or sent anywhere, but they may remain visible in your terminal history.



This is a learning project. Do not use it to make real security decisions. For real-world use, rely on a reputable password manager.





## License



This project is licensed under the MIT License. See the LICENSE file for details.

