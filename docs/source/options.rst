Options
=======

(development|production).ini settings

apex.session_secret = sess_secret
  REQUIRED, defines the session secret used for Pyramid

apex.auth_secret = auth_secret
  REQUIRED, defines the authentication secret used for Pyramid

apex.came_from_route = home
  REQUIRED, defines the default home route. Pyramid defaults to home, but
  some installations may use index, etc.

apex.velruse_config = %(here)s/CONFIG.yaml
  REQUIRED, location of the Velruse CONFIG.yaml file

apex.recaptcha_public_key = 
  OPTIONAL, REQUIRED if using Recaptcha

apex.recaptcha_private_key = 
  OPTIONAL, REQUIRED if using Recaptcha

apex.use_recaptcha_on_login = false
  OPTIONAL, Display Recaptcha form on Login Page

apex.use_recaptcha_on_forgot = false
  OPTIONAL, Display Recaptcha form on Forgot my Password Page

apex.use_recaptcha_on_reset = false
  OPTIONAL, Display Recaptcha form on Reset my Password Page

apex.use_recaptcha_on_register = true
  OPTIONAL, Display Recaptcha form on Registration Page

apex.provider_exclude = openid
  OPTIONAL, comma separated list to exclude configured providers

apex.apex_template = project:templates/auth.mako
  OPTIONAL, an optional template for rendering the authentication forms

apex.register_form_class = project.models.form_name
  OPTIONAL, requires DOTTED notation, specifies overloaded form for
  registration

apex.default_user_group = 
  OPTIONAL, If defined, will add the user to this group when created. If
  undefined, users will not be assigned to a group and you'll only have the
  permissions 'view' and 'authenticated'.

apex.sender_email = 
  OPTIONAL, defaults to nobody@example.com, 

apex.create_openid_before =
  OPTIONAL, NOT IMPLEMENTED, since OpenID requests don't allow us to
  override the signup form, we call this function before the OpenID
  Provider call.

apex.create_openid_after =
  OPTIONAL, since OpenID requests don't allow us to override the signup
  form, we call this function after the OpenID callback.

apex.openid_required =
  OPTIONAL, comma separated list of required fields when using OpenID to create
  an account

apex.default_groups = 
  OPTIONAL, comma separated list of group names to create. Defaults to 
  admin,user