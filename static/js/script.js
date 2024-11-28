/* JSHint directive that specifies $ as a global variable */
/* global $ */


/**
 * Delete BlogPost confirmation Modal
 * Set up event listeners for delete buttons, update the modal content,
 * and configure form submission for deleting posts.
 */
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap modal and form elements
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    const deleteForm = document.getElementById('deleteForm');
    
    // Handle delete button clicks
    document.querySelectorAll('.btn-delete').forEach(button => {
        button.addEventListener('click', function() {
            // Get post data from button attributes
            const postId = this.getAttribute('data-post-id');
            const postTitle = this.getAttribute('data-post-title');
            
            // Update modal content with post information
            document.querySelector('#deleteModalLabel').textContent = 'Delete Post';
            document.querySelector('.modal-body p').textContent = 
                `Are you sure you want to delete "${postTitle}"? This cannot be undone.`;
            
            // Set Form Action URL
            deleteForm.action = `/delete/${postId}/`;
            
            // Display Confirmation Modal
            deleteModal.show();
        });
    });
});


/**
 * Initializes jQuery UI's sortable functionality for the '#sortable' element.
 * Captures changes in the order of items.
 * Sends updated order information to the server via an AJAX POST request. 
 * 
 * The sortable functionality has been adapted from:
 * https://stackoverflow.com/questions/70809674/how-do-i-implement-jquery-ui-touch-punch-into-my-code
 * https://stackoverflow.com/questions/15633341/jquery-ui-sortable-then-write-order-into-a-database
 * https://jqueryui.com/sortable/
 * https://unpkg.com/browse/jquery-ui-touch-punch@0.2.3/
 * 
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
                url: '{% url "sort_posts" %}', // URL for the server endpoint
                data: {
                    'order[]': order, // Data to be sent, includes the new order of IDs
                    csrfmiddlewaretoken: '{{ csrf_token }}' // CSRF token for security
                },

                // Error Handling
                error: function(xhr, status, error) {
                    console.error('AJAX request failed:', error);
                }
            });
        }
    });
        // JQuery Touch Punch plugin modifies jQuery UI to support touch events
        $('#sortable').sortable('option', 'handle', '.sortable-handle');
});