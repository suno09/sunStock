<!-- logout modal -->
<div class="modal fade" id="modal-delete-user">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h4 class="modal-title" id='delete-modal-title'></h4>
        <button type="button" class="close" data-dismiss="modal" aria-label="Non">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form action="#" method="POST" id="form-delete-user">
          <div class="form-group row">
            <div class="col-sm-9">
              <p>Voulez-vous supprimer ce utilisateur ?</p>
            </div>
          </div>
          <input type="hidden" id="delete-id_user" name="id_user">
      </div>
      <div class="modal-footer justify-content-between">
        <button type="submit" class="btn btn-primary">Valider</button>
        <button type="reset" class="btn btn-default" data-dismiss="modal">Annuler</button>
      </div>
      </form>
    </div>
    <!-- /.modal-content -->
  </div>
  <!-- /.modal-dialog -->
</div>

<!-- jQuery -->
<script src="plugins/jquery/jquery.min.js"></script>

<script>
  $('#form-delete-user').submit(function(event) {
    event.preventDefault();
    $.ajax({
      url: "models/user.model.php",
      type: "post",
      timeout: 30000,
      data: "action=delete&" + $('#form-delete-user').serialize(),
      cache: false,
      success: function(response) {
        jresponse = JSON.parse(response);
        if (jresponse.type == 1) {
          notif('success', jresponse.message);
          setTimeout(function() {
            window.location.reload(false);
          }, 1000);
        } else {
          notif('error', jresponse.message);
        }
      },
      error: function() {
        notif('error', "Impossible d'effectuer la suppression !");
        setTimeout(function() {
          window.location.reload(false);
        }, 1000);
      },
    });
  });

  function init_form_delete_user(id_user) {
    $('#form-delete-user')[0].reset();
    $.ajax({
      url: "models/user.model.php",
      type: "post",
      timeout: 30000,
      data: "action=get_by_id&id_user=" + id_user,
      cache: false,
      success: function(response) {
        jresponse = JSON.parse(response);
        if (!jQuery.isEmptyObject(jresponse)) {
          $("#delete-id_user").val(jresponse.id_user);
          $("#delete-modal-title")[0].innerHTML = "Suppression Utilisateur: " + jresponse.username;
          $("#modal-delete-user").modal("show");
        } else {
          notif('error', 'Impossible charger la suppression !');
        }
      },
      error: function() {
        notif('error', 'Impossible charger la suppression !');
        setTimeout(function() {
          window.location.reload(false);
        }, 1000);
      },
    });
    return false;
  }
</script>