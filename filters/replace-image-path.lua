function Image(el)
    el.src = el.src:gsub("^assets/", "tmp/")
    el.src = el.src:gsub("./assets/", "tmp/")
    el.src = el.src:gsub("%.png$", "_png.jpg")

    return el
end
