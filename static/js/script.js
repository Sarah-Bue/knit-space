/**
 * Initializes jQuery UI's sortable functionality for the '#sortable' element.
 * Captures changes in the order of items.
 * Sends updated order information to the server via an AJAX POST request. 
 */
$(function() {
    // Enable sortable functionality using jQuery UI
    $('#sortable').sortable({
        // Event triggered when order of post has changed
        update: function(event, ui) {
            var order = [];
            // Create an array of post IDs in the new order
            $('#sortable li').each(function(index) {
                order.push($(this).data('id'));
            });
            // Send AJAX request to update the order on the server
            $.ajax({
                type: 'POST', // Use POST method
                url: '{% url "update_post_order" %}', // URL for the server endpoint
                data: {
                    order: order, // Data to be sent, includes the new order of IDs
                    csrfmiddlewaretoken: '{{ csrf_token }}' // CSRF token for security
                },

                // Error Handling
                error: function(xhr, status, error) {
                    console.error('AJAX request failed:', error);
                }
            });
        }
    });
});
