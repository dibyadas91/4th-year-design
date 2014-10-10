<html>
<p>EZSummarizer</p>
<form action="/upload" method="post" enctype="multipart/form-data">
  	<center>Query:      <input type="text" name="query" /></center>
	<br><center>Category:      <input type="text" name="category" /></center></br>
	<br><center>Degree of Dissimilarity:      <input type="text" name="degree" /></center></br>
  	<br><center>Select a file: <input type="file" name="upload" /></center></br>
  	<br><center><input type="submit" value="Start upload" /></center></br>
</form>

<div class="control-group">
    <label class="control-label">Threshold:</label>
    <div class="controls">
        <div id="fld_slider"></div>
        <input type="text" name="threshold" id="threshold" class="btn-mini" />
    </div>
  </div>

<script src="http://www.tools4noobs.com/js/jquery.ui.min.js"></script>
<script type="text/javascript>
/*initialize the slider*/
$(function() 
{
    $("#fld_slider").slider({
        range: "min",
        value: 70,
        min: 1,
        max: 100,
        slide: function(event, ui) 
        {
            $("#threshold").val(ui.value);
            repositionTooltip(event, ui);
        },
        stop: repositionTooltip
    });
    $("#fld_slider .ui-slider-handle:first").tooltip({
        title: $("#fld_slider").slider("value"),
        trigger: "manual"
    }).tooltip("show");
    $("#threshold").hide();
    $("#threshold").val($("#fld_slider").slider("value"));
});
</script><hr />
</html>
