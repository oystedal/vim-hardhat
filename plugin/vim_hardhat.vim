python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! Helmet()
python << endOfPython

from vim_hardhat import find_test_case_under_cursor

lines = vim.current.buffer[0:vim.current.window.cursor[0]]

test_case = find_test_case_under_cursor(lines)

if test_case != None:
    vim.command("Dispatch helmet \"" + test_case + "\"")
else:
    print("Could not find a helmet test")

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! Helmet call Helmet()
