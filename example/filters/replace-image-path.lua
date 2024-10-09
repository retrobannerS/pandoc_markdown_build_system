function Image(el)
    el.src = el.src:gsub("^assets/", "tmp/")
    el.src = el.src:gsub("./assets/", "tmp/")
    el.src = el.src:gsub("%.png$", ".jpg")

    return el
end
