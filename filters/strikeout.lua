function Strikeout(elem)
    return pandoc.RawInline('latex', '\\sout{' .. pandoc.utils.stringify(elem) .. '}')
end