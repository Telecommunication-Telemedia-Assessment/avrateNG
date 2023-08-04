
<!-- Latest compiled and minified JavaScript -->
<script src="/static/bootstrap.bundle.min.js"></script>

<!-- chart engine -->
<script src="/static/plotly-latest.min.js"></script>

<!-- prevent user from refreshing the page -->
% if get("use_noback", False):
<script src="/static/noback.js"></script>
% end
<script type="text/javascript">
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})
</script>
