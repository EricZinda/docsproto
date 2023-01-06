{% raw %}- 1\. **(Ensure Lisp/LKB reads grammar files using correct encoding)**
  
  - In grammar's global.lsp use the set-coding-system macro to set
the character encoding. Eg. (set-coding-system utf-8) at the top
of the file.
  - if running Allegro the following will then be executed
(setf excl:\*locale\* (excl::find-locale ".utf8"))
  - ISSUES: *canonical encoding (take from Emacs?), mapping into
encoding names used by specific Lisps, Lisp function
grammar-encoding must be written and incorporated into LKB code
base, backwards compatibility?*
- 2\. **(Ensure Emacs reads grammar files using correct encoding)**
  
  - In every grammar file require header
;;; -\*- Mode: TDL; Coding: utf-8 -\*-
  - ISSUES: *all files must have correct header, mulitbyte users
also need to load mule-ucs for emacs 21*
- 3\. **(Ensure Emacs and Lisp/LKB communicate in compatible and
sufficient character encoding)**
  
  - fi:common-lisp already takes care of this

Above assumes UTF-8 as the character encoding used of the grammar files.
This should be strongly recommended, but any other (GNU Emacs supported)
character encodings must also be allowed. Name used to specify character
encoding should be same in both 1 and 2 above.

Also:

- 4\. **(Links to PET, Lexdb and Lui settings)**

Also it might be friendly to mention some of the known issues:

- text input doesn't work for multibyte characters in CLIM;
- not all character sets display properly (e.g. Korean);
- do we need to add notes for versions compiled with ACL 6.2 (where
the encoding names are different)?
- postscript/LaTeX printing from CLIM/LUI with non-ascii characters.
<update date omitted for speed>{% endraw %}