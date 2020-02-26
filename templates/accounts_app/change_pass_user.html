<!-- edit user modal -->
<div class="modal fade" id="modal-password-user">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h4 class="modal-title" id='password-modal_title'>Changement mot de passe</h4>
        <button type="button" class="close" data-dismiss="modal" aria-label="Non">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form action="#" method="POST" id="form-password-user">
          <div class="form-group row">
            <label for="inputNewUsername" class="col-sm-3 col-form-label">Username</label>
            <div class="col-sm-9">
              <input type="text" class="form-control" placeholder="Username" id="password-username" name="username" disabled>
            </div>
          </div>
          <!-- <div class="form-group row">
            <label for="inputNewPassword" class="col-sm-3 col-form-label">Ancien mot de passe</label>
            <div class="col-sm-9">
              <input type="password" class="form-control" id="old-password" placeholder="Ancien mot de passe" name="old_password" required autofocus>
            </div>
          </div> -->
          <div class="form-group row">
            <label for="inputNewPassword" class="col-sm-3 col-form-label">Nouveau mot de passe</label>
            <div class="col-sm-9">
              <input type="password" class="form-control" id="new-password1" placeholder="Nouveau mot de passe" name="new_password1" required autofocus>
            </div>
          </div>
          <div class="form-group row">
            <label for="inputNewPassword" class="col-sm-3 col-form-label">Retaper nouveau mot de passe</label>
            <div class="col-sm-9">
              <input type="password" class="form-control" id="new-password2" placeholder="Retaper nouveau mot de passe" name="new_password2" required>
            </div>
          </div>
          <input type="hidden" id="password-id_user" name="id_user" >
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
  $('#form-password-user').submit(function(event) {
    event.preventDefault();
    var pass = $('#new-password1').val();
    var repass = $('#new-password2').val();

    if (pass != repass) {
        notif('error', "Retaper le mot de passe correctement");
        return false;
    }

    $.ajax({
      url: "models/user.model.php",
      type: "post",
      timeout: 30000,
      data: "action=update_pass&" + $('#form-password-user').serialize(),
      cache: false,
      success: function(response) {
        jresponse = JSON.parse(response);
        if (jresponse.type == 1) {
          notif('success', jresponse.message);
          setTimeout(function(){ window.location.reload(false); }, 1000);
        } else {
          notif('error', jresponse.message);
        }
      },
      error: function() {
        notif('error', "Impossible d'effectuer le changement !");
        setTimeout(function(){ window.location.reload(false); }, 1000);
      },
    });
  });

  function init_form_change_password(id_user) {
    $('#form-password-user')[0].reset();
    $.ajax({
      url: "models/user.model.php",
      type: "post",
      timeout: 30000,
      data: "action=get_by_id&id_user=" + id_user,
      cache: false,
      success: function(response) {
        jresponse = JSON.parse(response);
        if (!jQuery.isEmptyObject(jresponse)) {
            $("#password-id_user").val(jresponse.id_user);
            $("#password-username").val(jresponse.username);
            $("#modal-password-user").modal("show");          
        } else {
          notif('error', 'Impossible charger la modification !');
        }
      },
      error: function() {
        notif('error', 'Impossible charger la modification !');
        setTimeout(function(){ window.location.reload(false); }, 1000);
      },
    });
    return false;
  }
</script>