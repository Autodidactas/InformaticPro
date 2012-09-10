###
# codigo para placeholder
# en navegadores que no lo soporten
###
if !Modernizr.input.placeholder
    $('input[type="text"], input[type="password"], textarea').each ->
        placeholder = $(this).attr 'placeholder'

        $(this).attr('autofocus').blur()
        $(this).val placeholder

        $(this).on 'focus', ->
            if $(this).val() is placeholder
                $(this).val ''
        .on 'focusout', ->
            if $(this).val() is ''
                $(this).val placeholder

###
# manejo de campos requeridos
###
$('form').on 'submit', (e) ->
    $(this).find('*[required]').each ->
        placeholder = $(this).attr 'placeholder'
        if $(this).val() in [placeholder, '']
            e.preventDefault()
            error = if $(this).attr 'title' then $(this).attr 'title' else 'Campo requerido'
            $(this).after '<span class="form-error">' + error + '</span>'
    .on 'focus', ->
        $(this).next('.form-error').remove()

###
# abrir popups
###
#$('.popup .close').on 'click', ->
#    popup.close()
#
#$('[data-popup]').on 'click', ->
#    popup.open($(this).data 'popup')