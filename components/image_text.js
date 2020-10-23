function component(kwargs = {}) {
    var content, size;
    console.log(__name__, kwargs);
    content = kwargs.get("content");
    content = (content ? content.replace(" ", "+") : "Placeholder+text");
    size = kwargs.get("size");
    size = (size ? `${size}x${size}` : "128x128");
    return `
<div class="imgText">
<img src="https://via.placeholder.com/${size}.png?text=${content}"/>
<div>${kwargs.get("text")}</div>
</div>
`
;
}

//# sourceMappingURL=image_text.js.map
