{% raw %}## Parameters Related to Machine Translation Scoring

This page is a repository for information on translation ranking in the
Logon model.

    (setf *mt-analysis-weight* 0.2)  ; jacy
    (setf *mt-transfer-weight* 0.2)  ; mrs.blm
    (setf *mt-realization-weight* 0.2) ; Erik
    (setf *mt-lm-weight* 0.4) ; bnc.blm
    (setf *mt-distortion-weight* 0.0) ;  who knows?
    (setf *mt-lfn-weight* 0.0) ; lexical probabilities (source to target)
    (setf *mt-lnf-weight* 0.0) ; lexical probabilities (target to source)

## References

S. Oepen, E. Velldal, J.T. Lønning, P. Meurer, V Rosén, and D.
Flickinger [Towards Hybrid Quality-Oriented Machine Translation — On
Linguistics and Probabilities in
MT](http://www.velldal.net/erik/pubs/OepVelLon07.pdf) In Proceedings of
the 11th Conference on Theoretical and Methodological Issues in Machine
Translation (TMI-07), Skövde, Sweden, 2007
<update date omitted for speed>{% endraw %}