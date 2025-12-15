# Regex

**1. Regular Expressions for Text Processing:**

- Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
- The `re` module in Python is used for working with regular expressions.
- Common metacharacters: `.` (any character), `*` (zero or more), `+` (one or more), `?` (zero or one), `[]` (character class), `|` (OR), `^` (start of a line), `$` (end of a line), etc.
- Examples of regex usage: matching emails, phone numbers, or extracting data from text.
- `re` module functions include `re.match()`, `re.search()`, `re.findall()`, and `re.sub()` for pattern matching and replacement.

================

** What are Regex Metacharacters?
- Metacharacters are special symbols in regular expressions that define pattern-matching rules, not literal characters.
- They allow you to match variable text efficiently in logs, configs, and command outputs.

** Common Regex Metacharacters
- . (Dot) — Any Single Character
- Matches any one character except newline by default.
- DevOps use: Match variable hostnames, pod IDs, or IP octets.
- Example: node.       => Matches: node1, nodeA, node-

- * (Asterisk) — Zero or More
- Matches zero or more occurrences of the preceding character.
- DevOps use: Optional or repeated log fields.
- Example: error.*     => Matches: error, error123, error: disk full

- + (Plus) — One or More
- Matches at least one occurrence of the preceding character.
- DevOps use: Ensure something must exist (IDs, numbers).
- Example: [0-9]+       => Matches: 1, 42, 900

- ? (Question Mark) — Zero or One
- Makes the preceding character optional.
- DevOps use: Match optional flags or fields in logs.
- Example: https?        => Matches: http, https

- [] (Character Class)
- Matches one character from a set or range.
- DevOps use: Validate environment names, statuses, versions.
- Example: [A-Z]          => Matches: any uppercase letter

- | (Pipe) — OR Operator
- Matches either pattern A or pattern B.
- DevOps use: Match multiple log levels or services.

- ^ (Caret) — Start of Line
- Ensures the pattern starts at the beginning of a line.
- DevOps use: Identify log severity at line start.
- Example: ^ERROR

- $ (Dollar) — End of Line
- Ensures the pattern ends at the line’s end.
- DevOps use: Validate exact config values.
- Example: \.log$          => Matches files ending with .log

- 



