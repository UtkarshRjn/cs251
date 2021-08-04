# Bash

## What is a Bash Script

A Bash script is a plain text file which contains a series of commands. These commands are a mixture of commands we would normally type ouselves on the command line (such as ls or cp for example) and commands we could type on the command line but generally wouldn't.

**Anything you can run normally on the command line can be put into a script and it will do exactly the same thing. Similarly, anything you can put into a script can also be run normally on the command line and it will do exactly the same thing.**

It is convention to give files that are Bash scripts an extension of .sh (myscript.sh for example).Linux is an extensionless system so a script doesn't necessarily have to have this characteristic in order to work.

### How do bash scripts work

A program is a blob of binary data consisting of a series of  instructions for the CPU and possibly other resources (images, sound  files and such) organised into a package and typically stored on your  hard disk.  When we say we are running a program we are not really  running the program but a copy of it which is called a process.

Essentially a process is a running instance of a program.

### How to run them

Running a Bash script is fairly easy. Another term you may come across is executing the script (which means the same thing). Before we can execute a script it must have the execute permission set (for safety reasons this permission is generally not set by default). 

* [chmod](https://www.geeksforgeeks.org/chmod-command-linux/) - In Unix-like operating systems, the chmod command is used to change the access mode of a file.

```bash
./myscript.sh
bash: ./myscript.sh: Permission denied
    ls -l myscript.sh
-rw-r--r-- 18 ryan users 4096 Feb 17 09:12 myscript.sh
    chmod 755 myscript.sh
    ls -l myscript.sh
-rwxr-xr-x 18 ryan users 4096 Feb 17 09:12 myscript.sh
    ./myscript.sh
Hello World!

# Alternate way to run
bash myscript.sh
Hello World!
```

dot ( . ) is actually a reference to your current directory.

If we don't wrtie ./ ,Bash only looks in those specific directories and doesn't consider  sub directories or your current directory.  It will look through those  directories in order and execute the first instance of the program or  script that it finds.

#### \#!/bin/bash

This is the first line of the script above. The hash exclamation mark ( #! ) character sequence is referred to as the Shebang. Following it is the path to the interpreter (or program) that should be used to run (or interpret) the rest of the lines in the text file. (For Bash scripts it will be the path to Bash, but there are many other types of scripts and they each have their own interpreter.)

Formatting is important here. The shebang must be on the very first line of the file (line 2 won't do, even if the first line is blank). There must also be no spaces before the # or between the ! and the path to the interpreter.

## Variables

A variable is a temporary store for a piece of information. There are two actions we may perform for variables:

* Setting a value for a variable.
* Reading the value for a variable.

To read the variable we then place its name (preceded by a $ sign) anywhere in the script we would like. Before Bash interprets (or runs) every line of our script it first checks to see if any variable names are present. For every variable it has identified, it replaces the variable name with its value. Then it runs that line of code and begins the process again on the next line.

There are a few other variables that the system sets for you to use as well.

- **$0** - The name of the Bash script.
- **$1 - $9** - The first 9 arguments to the Bash script. (As mentioned above.)
- **$#** - How many arguments were passed to the Bash script.
- **$@** - All the arguments supplied to the Bash script.
- **$?** - The exit status of the most recently run process.
- **$$** - The process ID of the current script.
- **$USER** - The username of the user running the script.
- **$HOSTNAME** - The hostname of the machine the script is running on.
- **$SECONDS** - The number of seconds since the script was started.
- **$RANDOM** - Returns a different random number each time is it referred to.
- **$LINENO** - Returns the current line number in the Bash script.

```
If you type the command env on the command line you will see a listing of other variables which you may also refer to.
```

### Quotes

When we enclose our content in quotes we are indicating to Bash that  the contents should be considered as a single item.  You may use single  quotes ( ' ) or double quotes ( " ).

- Single quotes will treat every character literally.
- Double quotes will allow you to do substitution (that is include variables within the setting of the value).

```bash


    myvar='Hello World'
    echo $myvar
Hello World
    newvar="More $myvar"
    echo $newvar
More Hello World
    newvar='More $myvar'
    echo $newvar
More $myvar


```

### Command Subatitution

```bash
myvar=$( ls /etc | wc -l )
echo There are $myvar entries in the directory /etc

```

```
When playing about with command substitution it's a good idea to test your output rather than just assuming it will behave in a certain way. The easiest way to do that is simply to echo the variable and see what has happened. (You can then remove the echo command once you are happy.)
```

### Exporting variables

This introduces a phenomenon known as scope which affects variables amongst other things. The idea is that variables are limited to the process they were created in. Normaly this isn't an issue but sometimes, for instance, a script may run another script as one of its commands. If we want the variable to be available to the second script then we need to export the variable.

## User Inputs

### Piping

The operator we use is ( | ) (found above the backslash ( \ ) key on most keyboard
What this operator does is feed the output from the program on the  left as input to the program on the right. In the example below we will  list only the first 3 files in the directory.

## Arithmetic

### Let

**let** is a builtin function of Bash that allows us to do simple arithmetic.  It follows the basic format:

```comment
let <arithmetic expression>
```

### Expr

**expr** is similar to let except instead of saving the result to a variable it instead prints the answer.  Unlike **let** you don't need to enclose the expression in quotes.  You also must have spaces between the items of the expression.  It is also common to use **expr** within command substitution to save the output to a variable.

```comment
expr item1 operator item2
```

### Double Parenthese

```comment
$(( expression ))
```

```bash

#!/bin/bash
# Basic arithmetic using double parentheses
a=$(( 4 + 5 ))
echo $a # 9
a=$((3+5))
echo $a # 8
b=$(( a + 3 ))
echo $b # 11
b=$(( $a + 4 ))
echo $b # 12
(( b++ ))
echo $b # 13
(( b += 3 ))
echo $b # 16
a=$(( 4 * 5 ))
echo $a # 20

```

```output
9
8
11
12
13
16
20
```

### Length of a Variable

If we want to find out the lengh of a variable (how many characters) we can do the following:

```bash
${#variable}
```

## If Statement

### Test

The square brackets ( [ ] ) in the **if** statement above are actually a reference to the command **test**.  This means that all of the operators that test allows may be used here as well.

| Operator              | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| ! EXPRESSION          | The EXPRESSION is false.                                     |
| -n STRING             | The length of STRING is greater than zero.                   |
| -z STRING             | The lengh of STRING is zero (ie it is empty).                |
| STRING1 = STRING2     | STRING1 is equal to STRING2                                  |
| STRING1 != STRING2    | STRING1 is not equal to STRING2                              |
| INTEGER1 -eq INTEGER2 | INTEGER1 is numerically equal to INTEGER2                    |
| INTEGER1 -gt INTEGER2 | INTEGER1 is numerically greater than INTEGER2                |
| INTEGER1 -lt INTEGER2 | INTEGER1 is numerically less than INTEGER2                   |
| -d FILE               | FILE exists and is a directory.                              |
| -e FILE               | FILE exists.                                                 |
| -r FILE               | FILE exists and the read permission is granted.              |
| -s FILE               | FILE exists and it's size is greater than zero (ie. it is not empty). |
| -w FILE               | FILE exists and the write permission is granted.             |
| -x FILE               | FILE exists and the execute permission is granted.           |

A few points to note:

- **=** is slightly different to **-eq**.  [ 001 = 1 ] will return false as = does a string comparison (ie. character for character the same) whereas -eq does a numerical comparison meaning [ 001 -eq 1 ] will return true.
- When we refer to FILE above we are actually meaning a [path](https://ryanstutorials.net/linuxtutorial/navigation.php).  Remember that a path may be absolute or relative and may refer to a file or a directory.
- Because [ ] is just a reference to the command **test** we may experiment and trouble shoot with test on the command line to make sure our understanding of its behaviour is correct.

## Loops

```bash

#!/bin/bash
# Basic while loop
counter=1
while [ $counter -le 10 ]
do
echo $counter
((counter++))
done
echo All done

```

A common mistake is what's called an **off by one** error.  In the  example above we could have put -lt as opposed to -le  (less than as  opposed to less than or equal). Had we done this it would have printed  up until 9.  These mistakes are easy to make but also easy to fix once  you've identified it so don't worry too much if you make this error.

### Select

The select mechanism allows us to create a simple menu system. It has the following format:

```bash
select var in <list>
do
<commands>
done
```

When invoked it will take all the items in **list** (similar to other loops this is a space separated set of items) and present them on the screen with a number before each item. A prompt will be printed after this allowing the user to select a number.  When they select a number and hit *enter* the corresponding item will be assigned to the variable **var** and the commands between do and done are run.

A few points to note:

- No error checking is done.  If the user enters something other than a number or a number not corresponding to an item then **var** becomes null (empty)
- If the user hits *enter* without entering any data then the list of options will be displayed again.
- The loop will end when an EOF signal is entered or the break statement is issued.
- You may change the system variable **PS3** to change the prompt that is displayed.

## Functions

Instead of writing out the same code over and over you may write it once in a function then call that function every time.

They may be written in two different formats:

```bash
function_name () {
	<commands>
}
```

```bash
function function_name {
	<commands>
}
```

*  In other programming languages it is common to have arguments passed to  the function listed inside the brackets ().  In Bash they are there only for decoration and you never put anything inside them.

* The function definition ( the actual function itself) must appear in the script before any calls to the function.

### Passing arguments through a function

```bash
#!/bin/bash
# Passing arguments to a function
print_something () {
	echo Hello $1
}
print_something Mars
print_something Jupiter

```

```output
Hello Mars
Hello Jupiter
```

### Return Values

Most other programming languages have the concept of a return value for  functions,  a means for the function to send data back to the original  calling location. Bash functions don't allow us to do this.

To get  a return from the function we can use command substitution and have the function print the result (and only the result)

```bash
#!/bin/bash
# Setting a return value to a function
lines_in_file () {
cat $1 | wc -l
}
num_lines=$( lines_in_file $1 )
echo The file $1 has $num_lines lines in it.

```

 ### Variable Scope

Scope refers to which parts of a script can see which variables.  By default a variable is **global**.  This means that it is visible everywhere in the script.   We may also create a variable as a **local** variable.  When we  create a local variable within a function, it is only visible within  that function.  To do that we use the keyword **local** in front of the variable the first time we set it's value.

```bash
local var_name=<var_value>
```

### Overriding commands

It is possible to name a function as the same name as a command you  would normally use on the command line.  This allows us to create a  wrapper.  eg. Maybe every time we call the command **ls** in our script, what we actually want is **ls -lh**.  We could do the following:

```bash
#!/bin/bash
# Create a wrapper around the command ls

ls () {
	command ls -lh
}

ls
```

If we didn't put the keyword **command** in front of ls on line 5  we would end up in an endless loop.  Even though we are inside the  function ls when we call ls it would have called another instance of the function ls which in turn would have done the same and so on.

```
It's easy to forget the command keyword and end up in an endless loop. If you encounter this then you can cancel the script from running by pressing the keys CTRL c at the same time on your keyboard. CTRL c is a good way to cancel your script (or a program) whenever you get into trouble on the command line.
```

## User Interface

### tput

t-put is a command which allows you to control the cursor on the terminal and the format of content that is printed.  It is quite a powerful and  complex tool.

### Supplying data

There are 3 ways in which you may supply data to a Bash script:

- As command line arguments
- Redirected in as STDIN
- Read interactively during script execution

Command line arguments are good as they will be retained in the users history making it easy for them to rerun commands.  Command line arguments are also convenient when the script is not run  directly by the user (eg, as part of another script or a cron task etc).

Redirected from STDIN is good when your script is behaving like a filter and just modifying or reformatting data that is fed to it.

Reading interactively is good when you don't know what data may be  required until the script is already running. eg. You may need to  clarify some suspicious or erroneous input.  Passwords are also ideally  asked for this way so they aren't kept as plain text in the users  history.

## Wget

Wget is the non-interactive network downloader which is used to download files from the server even when the user has not logged on to the  system and it can work in the background without hindering the current  process.

* wget is non-interactive, meaning that it can work in the background,  while the user is not logged on. This allows you to start a retrieval  and disconnect from the system, letting wget finish the work. By  contrast, most of the Web browsers require constant user’s presence,  which can be a great hindrance when transferring a lot of data.

[download.sh solution](https://stackoverflow.com/questions/17282915/how-to-download-an-entire-directory-and-subdirectories-using-wget/)

## [Hard and Soft Link](https://www.geeksforgeeks.org/soft-hard-links-unixlinux/)

[ln command](https://www.geeksforgeeks.org/ln-command-in-linux-with-examples/)

A link in UNIX is a pointer to a file. Like pointers in any programming  languages, links in UNIX are pointers pointing to a file or a directory. Creating links is a kind of shortcuts to access a file.

There are two types of links :

1. Soft Link or Symbolic links
2. Hard Links

### Hard Link

* Each hard linked file is assigned the same Inode value as the original,  therefore they reference the same physical file location. Hard links  more flexible and remain linked even if the original or linked files are moved throughout the file system, although hard links are unable to  cross different file systems.

* We cannot create a hard link for a directory to avoid recursive loops.
* Even if we change the filename of the original file then also the hard links properly work.
* Removing any link, just reduces the link count, but doesn’t affect other links.
* ls -l command shows all the links with the link column shows number of links.

### Soft Link

* A soft link is similar to the file shortcut feature which is used in  Windows Operating systems. Each soft linked file contains a separate Inode value that points to the original file. As similar to hard links, any changes to the data in either file is reflected in the other. Soft links can be linked across different file systems, although if the  original file is deleted or moved, the soft linked file will not work  correctly (called hanging link).
* ls -l command shows all links with first column value l? and the link points to original file.
* Soft Link contains the path for original file and not the contents.
* Removing soft link doesn’t affect anything but removing original file,  the link becomes “dangling” link which points to nonexistent file.
* A soft link can link to a directory.
* Size of a soft link is equal to the name of the file for which the soft  link is created. E.g If name of file is file1 then size of it’s soft  link will be 5 bytes which is equal to size of name of original file.
* If we change the name of the original file then all the soft links for that file become dangling i.e. they are worthless now.
* Link across file systems: If you want to link files across the file systems, you can only use symlinks/soft links.
