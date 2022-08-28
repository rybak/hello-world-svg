generated.svg: generate.py
	./generate.py >$@

output.svg: begin.svg generated.svg end.svg
	cat $^ >$@
