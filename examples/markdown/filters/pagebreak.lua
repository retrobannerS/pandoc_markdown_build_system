function Para (elem)
  if elem.content[1].text == 'BREAK__' then
    return pandoc.RawBlock('latex', '\\newpage')
  end
  return elem
end