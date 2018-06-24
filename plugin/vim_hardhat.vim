python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! RunTest()
python << endOfPython

from vim_hardhat import find_test_case_under_cursor

lines = vim.current.buffer[0:vim.current.window.cursor[0]]
test_case = find_test_case_under_cursor(lines)

if test_case != None:
    command = "AsyncRun ./build/run_test " + test_case
    vim.command(command)
else:
    print("Could not find test case")

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! RunTest call RunTest()
