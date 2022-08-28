
output.svg: begin.svg generated.svg end.svg
	cat $^ >$@

generated.svg: generate.py
	./generate.py >$@

