
function mascaraTelefone(input) {
                    var v = input.value.replace(/\D/g, '');
                    v = v.replace(/^(\d{2})(\d)/g, '($1) $2');
                    v = v.replace(/(\d{5})(\d)/, '$1-$2');
                    input.value = v;
}
