{% raw %}# Chart Pruning Investigation

We tried a range of chart pruning options over both the cb and sc01
profiles, and compared performance and coverage against two control
cases:

- none180: no chart pruning, timeout=180 (configuration used to
produce gold profiles)
- none60: no chart pruning, more realistic timeout of 60 seconds

Along with the standard coverage and average parse times, the statistics
were are interested in are:

- how often the top parse is lost due to pruning; and
- how often the gold parse is lost due to pruning

All the chart pruning parse runs used the CPU, with the 1111 version of
the ERG

-       (pvm:make-cpu
                :host (short-site-name)
                :spawn (logon-file "bin" "cheap" :string)
                    :options (list "-tsdb" "-packing"
                      "-repp" "-tagger" "-cm" "-default-les=all"
                      "-memlimit=1024" "-timeout=60"
                      "-cp=${cpopt}"
                      (registry:lookup :erg "~a~a~a" :ln :rt :cp))
                 :class :tempcpu :grammar (registry:lookup :erg "ERG (~a)" :vn) 
                 :name "pet-cp"
                 :task '(:parse)  :flags '(:generics t)
                 :wait 300 :quantum 180) 

Results are available on Google Docs
[here](https://docs.google.com/spreadsheet/ccc?key=0An2fnG5kbAcodFJjcDQ4VDc5enBHWC1mT0NZZUFwSXc).
One subtlety in these numbers is the treatment of items which had
results, but also had a "timed out" error. Since we are interested in
getting the exact right result, these items are treated as if they
produced zero readings when calculating coverage etc.
<update date omitted for speed>{% endraw %}