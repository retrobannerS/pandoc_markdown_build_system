function Underline(elem)
    return pandoc.RawInline('latex', '\\underline{' .. pandoc.utils.stringify(elem) .. '}')
end