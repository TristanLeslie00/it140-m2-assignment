<!-- To see this file in a clean, formatted view, select ▼ in the upper-right corner of the editor pane, then select "Markdown Preview". -->

# Construct Phase

**SDLC progress:** [0 Start Here](../README.md) → [1 Analyze](../analysis/README.md) → [2 Design](../design/README.md) → **3 Construct** → [4 Test](../tests/README.md) → [5 Submit](https://learn.snhu.edu/)

<!-- omit from toc -->
## Table of Contents

* [Purpose](#purpose)
* [Deliverable](#deliverable)
* [What You Will Use](#what-you-will-use)
* [What You Will Do](#what-you-will-do)
* [Check Your Work](#check-your-work)
* [Help and Support](#help-and-support)
* [Next Steps](#next-steps)

## Purpose

During the Construct phase, you turn the provided design into a working Python program.

You will complete the [`name_age.py`](./name_age.py) starter file in small steps. Use your [Software Development Worksheet (SDW)](../name_age_sdw.md) and the provided [pseudocode](../design/name_age.pseudo) to guide your work.

This starter file contains more Python structure than programs you have seen so far. Some of that structure uses concepts you have not learned yet. **You are not expected to understand or write all of it yet.** The provided structure is complete; your work is limited to the lines marked `TODO:`.

### Edit Only TODO Lines

**Only change lines marked with `TODO:`.**

This includes:

* `TODO:` lines inside the module docstring
* `# TODO:` comment lines inside `main()`
* `# TODO:` lines in the References section

Do not change any other lines of code in the starter file, including the imports, constants, main function definition, main guard, or other provided code. You may cause a Python syntax error if you change those lines and your program will not run.

When you replace a `# TODO:` line inside `main()`, keep your new code at the **same indentation level** as the TODO comment. Indentation is important in Python. The starter file uses four spaces for indentation inside `main()`.

## Deliverable

**This phase produces a deliverable.**

You will complete [`name_age.py`](./name_age.py) during this phase. After completing the Test phase, you will submit this file in **D2L Brightspace** for grading as part of the Module Two Assignment.

The Module Two Assignment also includes a separate **IDE Features Reflection** deliverable. You will complete that separately.

## What You Will Use

Use the following provided materials to complete this phase:

* [`name_age.py`](./name_age.py) — the Python starter file you will complete and later submit for grading.
* [Software Development Worksheet (SDW)](../name_age_sdw.md) — contains your Analyze and Design working notes.
* [Pseudocode](../design/name_age.pseudo) — provides a step-by-step, programming-language-independent description of the solution.
* [Software Design Document (SDD)](../design/name_age_sdd.md) — explains how the solution is designed.
* [Software Requirements Specification (SRS)](../analysis/name_age_srs.md) — defines what the completed program must do.

Relevant zyBooks topics include:

* **1.3 Basic input and output**
* **1.13 Variables and assignments**
* **1.14 Identifiers**
* **1.16 Arithmetic expressions**
* **1.17 Python expressions**
* **1.19 Module basics**
* **1.20 Math module**
* **2.6 Type conversions**
* **2.7 String formatting**

## What You Will Do

### 1. Read the Starter File Before Editing

Open [`name_age.py`](./name_age.py) and read it from beginning to end before making changes.

The file is organized into the following parts:

| Part | What to do in this assignment |
| --- | --- |
| Module docstring | Replace its `TODO:` lines with your own documentation. |
| Imports | Read the provided code, but do not change it. |
| Constants | Read the provided code, but do not change it. |
| Main function | Replace only its four `# TODO:` lines with indented Python statements. |
| Main guard | Read the provided code, but do not change it. |
| References | Replace or delete its `# TODO:` lines as directed in Step 10. |

This organization helps make a Python source file easier to read. The large section-header comments are **instructional scaffolding** that identify the parts of your first structured Python module. Professional Python code normally relies more on conventional ordering, descriptive names, blank lines, and smaller comments.

The rest of these instructions explain what you must know to complete the assignment. If you are curious about how all the provided parts work, see [Understanding the Name and Age Starter File](https://github.com/GC-STEM/it140-m2-assignment/wiki/Understanding-the-Name-and-Age-Starter-File) in the assignment wiki.

### 2. Complete the Module Docstring

The triple-quoted text at the beginning of `name_age.py` is a **module documentation string**, usually called a **module docstring**.

A module docstring explains the purpose and use of the Python module. Python's [**PEP 257 — Docstring Conventions**](https://peps.python.org/pep-0257/) recommends that a multi-line docstring begin with a short summary, followed by a blank line and additional information.

The starter docstring follows that basic pattern but adds several instructional sections:

* **Input** — data the program needs, including its type and source
* **Process** — how the program transforms input into output
* **Output** — what the program produces and where it goes
* **Typical usage example** — an example of the program being used

The Input → Process → Output structure is an IT 140 learning convention. It is not a required PEP 257 docstring format.

#### Use Your SDW

You have already done most of the thinking needed for the docstring in your Software Development Worksheet (SDW). Use your SDW to complete the module docstring in `name_age.py`. These sections may be particularly useful:

* Use **SDW 2. Program Purpose** for the one-line summary.
* Use **SDW 3. IPO: Inputs** for the `Input:` section.
* Use **SDW 3. IPO: Processing** for the `Process:` section.
* Use **SDW 3. IPO: Outputs** for the `Output:` section.
* Use your understanding of the SRS and test examples to create a **new, original** usage example.

Do not copy the SRS sample or an acceptance test case for your usage example. Choose your own example values and determine the correct result.

#### Write the Docstring Yourself

Write the module docstring **in your own words**. Do not copy text from the SRS, SDD, another source, or another person, and do not use an AI tool to generate it.

AI-assisted programming can help produce code quickly, but software developers must still be able to understand and explain what their programs do, what data they use, how they process that data, and what results they produce. Writing this short docstring yourself demonstrates that you understand the program you are constructing.

Only replace the lines in the Python file marked `TODO:`. Keep the provided headings and triple quotation marks (`"""`) unchanged.

### 3. Recognize the Import

The starter file provides this import:

```python
from datetime import date
```

It makes Python's `date` class available to the program. The provided constant in Step 4 uses `date.today()` to get the computer's current local date.

You do not need to write or change this line. To learn more, see [Importing `date`](https://github.com/GC-STEM/it140-m2-assignment/wiki/Understanding-the-Name-and-Age-Starter-File#importing-date).

### 4. Recognize the Constant

The starter file provides this constant:

```python
CURRENT_YEAR = date.today().year
```

It gets the current year from the computer and stores it as an integer. Your code will use `CURRENT_YEAR` in the required calculation. This is why your SDW treats the current year as an input the program **obtains internally**, even though the user does not type it.

You do not need to write or change this line. To learn more, see [The `CURRENT_YEAR` constant](https://github.com/GC-STEM/it140-m2-assignment/wiki/Understanding-the-Name-and-Age-Starter-File#the-current_year-constant).

### 5. Recognize the Documentation and Comments

The starter file uses a module docstring, a function docstring, block comments, an inline comment, and instructional section-header comments. Only the marked `TODO:` lines require your work.

You will complete the module docstring in Step 2, replace the four code TODO comments in Step 8, and complete or delete the reference TODO comments in Step 10. Leave the other documentation and comments unchanged.

To learn how these forms of documentation differ, see [Documentation and comments](https://github.com/GC-STEM/it140-m2-assignment/wiki/Understanding-the-Name-and-Age-Starter-File#documentation-and-comments).

### 6. Work Inside the Main Function

All four Python statements you write for this assignment go inside the provided `main()` function:

```python
def main() -> None:
    """Run the name-age program."""

    # TODO: Replace with code here.
```

Do not change the `main()` definition or its docstring. Replace each code TODO comment while keeping the same four-space indentation. The indentation shows Python that your statement belongs inside `main()`.

You will learn how to define functions later in the course. To learn more now, see [The `main()` function](https://github.com/GC-STEM/it140-m2-assignment/wiki/Understanding-the-Name-and-Age-Starter-File#the-main-function).

### 7. Leave the Main Guard Unchanged

Near the bottom of the file, the provided **main guard** starts the `main()` function when you run `name_age.py` directly:

```python
if __name__ == "__main__":
    main()
```

You do not need to write or change either line. Keep `main()` indented beneath the `if` statement.

You will learn about `if` statements and functions later in the course. To learn more now, see [The main guard](https://github.com/GC-STEM/it140-m2-assignment/wiki/Understanding-the-Name-and-Age-Starter-File#the-main-guard).

### 8. Write the Program One TODO at a Time

Now complete the `# TODO:` lines inside `main()`.

Use the [pseudocode](../design/name_age.pseudo) as your primary coding guide. Note that pseudocode is not Python code. You will need to translate the pseudocode into correct Python syntax for your program to work.

#### Get the User's Name

Replace:

```python
# TODO: Replace with code to get user's name as a string. See zyBooks 1.3.
```

Use concepts from **zyBooks 1.3, Basic input section**.

#### Get the User's Age

Replace:

```python
# TODO: Replace with code to get user's age as an integer. See zyBooks 2.6.
```

Remember that `input()` provides text (i.e., a string). The program needs the age as an integer because it will use the age in arithmetic.

Review **zyBooks 2.6 Type conversions** if needed.

#### Calculate the Birth Year

Replace:

```python
# TODO: Replace with code to process data. See zyBooks 1.16 & 1.17.
```

Use your SRS, SDD, pseudocode, and SDW to determine the required arithmetic expression.

#### Display the Result

Replace:

```python
# TODO: Replace with code to output formatted results. zyBooks 1.3 & 2.7.
```

Review **zyBooks 1.3 Basic input and output** and **2.7 String formatting** if needed. We strongly recommend using an f-string for this output as introduced in zyBooks 2.7.

### 9. Run After Each Small Change

This activity depends on correct Python syntax and indentation.

Work incrementally:

1. Replace one code TODO.
2. Run the program.
3. Correct any syntax or other errors.
4. Continue to the next TODO only after the program runs again.

This makes it much easier to identify which recent change caused a problem.

Pay particular attention to:

* Matching quotation marks
* Matching parentheses
* Four-space indentation inside `main()`
* Variable-name spelling
* Correct use of `=`
* Correct placement of function calls such as `input()`, `int()`, and `print()`

> [!NOTE]
> **A spell-check underline does not necessarily mean there is an error.**
>
> The course IDE includes a spell checker that marks words it does not recognize with a blue squiggly underline. Names, technical terms, and other correctly spelled words may not be in the spell checker's dictionary.
>
> When you see a blue squiggly underline:
>
> 1. Check whether the word is spelled correctly.
> 2. If it is misspelled, correct it.
> 3. If it is spelled correctly, you can ignore the underline or add the word to the spell checker's dictionary by hovering your pointer over the word and selecting **Quick Fix**.
>
> A spell-check suggestion does **not** mean that your Python program contains an error.

### 10. Complete the References Section

The final section of the starter file is:

```python
# === References ===
# TODO: Replace with an APA-style reference for a source you used, or delete.
# TODO: Replace with another APA-style reference, or delete this TODO line.
```

The References section is an **SNHU course convention**, not a requirement of Python or PEP 8.

Software developers regularly build on documentation, libraries, examples, tools, and the work of other people. Professional practice requires respecting applicable attribution, licensing, organizational, and disclosure requirements. IT 140 uses the References section to build the habit of keeping the sources that influenced your work visible with the code.

Add APA-style references for outside sources you used beyond the provided course materials, including applicable:

* Documentation or websites
* Code examples
* IDE inline code suggestions
* AI chats or coding agents
* Other people or external resources that contributed to your solution

Do not add references merely because a source exists. Reference sources that you actually used.

If you did not use additional sources, delete the unused `# TODO:` reference lines.

The **module docstring remains your own original writing**, even if AI assistance is allowed for other parts of your work.

> **IDE Features Reflection reminder:** As you construct the program, notice how VS Code features such as syntax highlighting, code completion, indentation guides, and error indicators affect your work. Your observations may help when you complete the separate [IDE Features Reflection](../../Part-B/ide_features.md).

## Check Your Work

Before continuing to the Test phase, make sure:

* [ ] I changed only lines marked with `TODO:`.
* [ ] I completed the module docstring in my own words.
* [ ] My module docstring describes the program's input, process, and output.
* [ ] My usage example uses original values rather than copying a provided example.
* [ ] I left the import, constant, `main()` definition, and main guard unchanged.
* [ ] My Python code inside `main()` remains indented four spaces.
* [ ] I used the provided pseudocode as my coding guide.
* [ ] I ran the program after making small changes and corrected syntax errors.
* [ ] I added references for outside sources I used or deleted unused reference TODOs.
* [ ] No `TODO:` lines remain in my completed file.
* [ ] I saved `name_age.py` and can run it without a Python error.

## Help and Support

If you have difficulty completing this phase:

* Start with the [pseudocode](../design/name_age.pseudo) and work on one TODO at a time.
* Review your [SDW](../name_age_sdw.md) for the program's purpose, IPO, requirements, and design connections.
* Refer to the [SRS](../analysis/name_age_srs.md) when you need to confirm what the program must do.
* Review the relevant zyBooks sections identified next to each starter-code TODO.
* See the [Module Two Assignment Wiki](https://github.com/GC-STEM/it140-m2-assignment/wiki) for supplemental programming and course-IDE guidance.
* Use [GitHub Discussions](https://github.com/GC-STEM/it140-m2-assignment/discussions) for questions about using the repository.
* Use [GitHub Issues](https://github.com/GC-STEM/it140-m2-assignment/issues) to report a technical problem with the provided files or tools.
* Contact your instructor through D2L Brightspace for questions about assignment requirements, grading, or feedback.

## Next Steps

When you have completed the Construct phase and your program runs without a Python syntax error, continue to the [Test](../tests/README.md) phase.

<!-- Artifact Metadata
* Course: IT 140 - Introduction to Scripting
* Artifact Title: 2-3 Module Two Assignment | Construct Phase
* Artifact Type: Required assignment guidance; phase produces the graded name_age.py deliverable
* Artifact Purpose: Guide students through constructing the Module Two name_age Python program from the provided design and starter file.
* Artifact Description: Students learn the structure of the provided Python module, complete only marked TODO lines, document the program in their own words, construct the required program incrementally, and prepare it for formal testing.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}
-->
