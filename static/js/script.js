/* JSHint directive that specifies $ as a global variable */
/* global $ */

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
                url: '{% url "sort_posts" %}', // URL for the server endpoint
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
        // JQuery Touch Punch plugin modifies jQuery UI to support touch events
        $('#sortable').sortable('option', 'handle', '.sortable-handle');
});

/**
 * Manages the deletion modal functionality for blog posts.
 * Handles click event on delete buttons, updates modal content,
 * and displays confirmation dialog to user.
 */
$(document).ready(function() {
    // Handle delete button click
    $(document).on('click', '.delete-post', function(e) {
        e.preventDefault();
        var postId = $(this).data('id');
        var postTitle = $(this).data('title');
        var deleteUrl = $(this).data('url');
        
        // Update modal content
        $('#deleteModal .modal-title').text('Delete Post');
        $('#deleteModal .modal-body').text('Are you sure you want to delete "' + postTitle + '"?');
        $('#deleteModal form').attr('action', deleteUrl);
        
        // Show modal
        $('#deleteModal').modal('show');
    });
});