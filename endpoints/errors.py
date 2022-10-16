from fastapi import  HTTPException, status



def check_is_superuser(current_user):
	if not current_user.is_superuser:
	        raise HTTPException(
	            status_code=status.HTTP_401_UNAUTHORIZED,
	            detail="Not enough rights to create a product",
	        )


def check_product_id_category(category_product):
	if not category_product:
        	raise HTTPException(
	        	status_code=status.HTTP_404_NOT_FOUND, 
	        	detail="No such product category was found"
	    	)

def check_404(arg):
	if arg is None:
	        raise HTTPException(
	            status_code=status.HTTP_404_NOT_FOUND, detail="Not found"
	        )